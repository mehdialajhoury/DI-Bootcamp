import os
import json
import logging
import asyncio
from typing import List, Dict, Any, AsyncGenerator

from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from contextlib import AsyncExitStack

from groq import Groq, BadRequestError # On importe l'erreur spécifique
import ollama

# Charger les variables d'environnement
load_dotenv()

# --- DIAGNOSTIC AU DÉMARRAGE ---
print("--- DÉBUT DIAGNOSTIC ---")
token = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")
if not token:
    print("ERREUR FATALE : GITHUB_PERSONAL_ACCESS_TOKEN est vide ou introuvable dans .env")
else:
    print(f"Token GitHub trouvé : {token[:4]}...")

base_dir = os.getenv("ALLOWED_DIR", "./workspace")
abs_path = os.path.abspath(base_dir)

if not os.path.exists(abs_path):
    print(f"Le dossier '{abs_path}' n'existait pas, création en cours...")
    os.makedirs(abs_path, exist_ok=True)
else:
    print(f"Dossier Workspace détecté : {abs_path}")
print("--- FIN DIAGNOSTIC ---")


# --- 1. Custom Tool ---
def local_sentiment_analysis(text: str) -> str:
    text = text.lower()
    if any(x in text for x in ["crash", "broken", "emergency", "fatal"]):
        return "Critical Priority"
    elif any(x in text for x in ["bug", "error", "fail", "wrong"]):
        return "Warning"
    return "Neutral/Info"

# --- 2. The Agent Class ---
class MCPAgent:
    def __init__(self):
        self.provider = os.getenv("LLM_PROVIDER", "groq")
        
        # --- FIX STRICT : On interdit formellement la simulation ---
        system_prompt = (
            "You are a Research Commander. You have access to GitHub, a Filesystem, and a Local Analysis tool. "
            "Plan your steps. Always fetch data first, analyze it, then save it. "
            "CRITICAL RULES:"
            "1. You must use the tools provided to get REAL data."
            "2. Do NOT simulate or guess what the tool will return."
            "3. Do NOT make assumptions like 'Assuming the response is...'."
            "4. When you call a tool, STOP speaking and wait for the result."
            "5. Use standard JSON format for tool calls."
        )
        
        self.history = [{"role": "system", "content": system_prompt}]
        
        if self.provider == "groq":
            self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    async def run_process(self, user_prompt: str) -> AsyncGenerator[Dict, None]:
        self.history.append({"role": "user", "content": user_prompt})

        # Config Serveurs
        github_params = StdioServerParameters(
            command="npx",
            args=["@modelcontextprotocol/server-github"],
            env={**os.environ}
        )
        
        fs_params = StdioServerParameters(
            command="npx",
            args=["@modelcontextprotocol/server-filesystem", abs_path],
            env={**os.environ}
        )

        try:
            async with AsyncExitStack() as stack:
                yield {"type": "log", "content": "Tentative de connexion aux serveurs MCP..."}
                
                # 1. Start GitHub
                try:
                    gh_read, gh_write = await stack.enter_async_context(stdio_client(github_params))
                    gh_session = await stack.enter_async_context(ClientSession(gh_read, gh_write))
                    await gh_session.initialize()
                    yield {"type": "log", "content": "GitHub connecté."}
                except Exception as e:
                    print(f"ERREUR GITHUB DETAILEE: {e}")
                    raise e

                # 2. Start Filesystem
                try:
                    fs_read, fs_write = await stack.enter_async_context(stdio_client(fs_params))
                    fs_session = await stack.enter_async_context(ClientSession(fs_read, fs_write))
                    await fs_session.initialize()
                    yield {"type": "log", "content": "Filesystem connecté."}
                except Exception as e:
                    print(f"ERREUR FILESYSTEM DETAILEE: {e}")
                    raise e

                # Tool Aggregation
                tools = []
                tool_map = {}

                def add_tools(mcp_tools, session):
                    for t in mcp_tools.tools:
                        tools.append({
                            "type": "function",
                            "function": {
                                "name": t.name,
                                "description": t.description,
                                "parameters": t.inputSchema
                            }
                        })
                        tool_map[t.name] = session

                gh_tools = await gh_session.list_tools()
                fs_tools = await fs_session.list_tools()
                
                add_tools(gh_tools, gh_session)
                add_tools(fs_tools, fs_session)

                tools.append({
                    "type": "function",
                    "function": {
                        "name": "local_sentiment_analysis",
                        "description": "Analyze text priority/sentiment.",
                        "parameters": {"type": "object", "properties": {"text": {"type": "string"}}, "required": ["text"]}
                    }
                })

                yield {"type": "log", "content": f"  {len(tools)} outils chargés. Début du raisonnement..."}

                # Reasoning Loop
                while True:
                    # Appel LLM avec gestion d'erreur spécifique Groq
                    try:
                        raw_response = self._call_llm(tools)
                    except BadRequestError as e:
                        error_msg = str(e)
                        if "tool_use_failed" in error_msg:
                            yield {"type": "log", "content": "L'IA a mal formaté sa demande. Nouvelle tentative..."}
                            # On ajoute un rappel à l'ordre dans l'historique et on continue
                            self.history.append({"role": "user", "content": "Error: You used an invalid format. Do not use XML. Use JSON tool calls."})
                            continue
                        else:
                            raise e

                    # Nettoyage pour Groq (Anti-Bug annotations)
                    clean_response = {
                        "role": raw_response["role"],
                        "content": raw_response.get("content")
                    }
                    if raw_response.get("tool_calls"):
                        clean_response["tool_calls"] = raw_response["tool_calls"]
                    
                    self.history.append(clean_response)
                    response_msg = clean_response

                    if not response_msg.get("tool_calls"):
                        yield {"type": "answer", "content": response_msg["content"]}
                        break

                    for tool_call in response_msg["tool_calls"]:
                        fn_name = tool_call["function"]["name"]
                        fn_args = json.loads(tool_call["function"]["arguments"])
                        
                        yield {"type": "log", "content": f"Exécution : **{fn_name}**"}
                        
                        try:
                            if fn_name == "local_sentiment_analysis":
                                result = local_sentiment_analysis(fn_args["text"])
                            elif fn_name in tool_map:
                                mcp_res = await tool_map[fn_name].call_tool(fn_name, arguments=fn_args)
                                result = mcp_res.content[0].text
                            else:
                                result = "Error: Tool not found."
                        except Exception as e:
                            result = f"Error executing tool: {str(e)}"
                            yield {"type": "log", "content": f"Erreur outil : {result}"}

                        self.history.append({
                            "role": "tool",
                            "tool_call_id": tool_call["id"],
                            "name": fn_name,
                            "content": str(result)
                        })
                        
        except Exception as e:
            print(f"ERREUR CRITIQUE DANS L'AGENT : {e}")
            if hasattr(e, 'exceptions'):
                for i, sub_e in enumerate(e.exceptions):
                    print(f"SOUS-ERREUR {i+1}: {sub_e}")
            import traceback
            traceback.print_exc()
            raise e

    def _call_llm(self, tools):
        if self.provider == "groq":
            res = self.client.chat.completions.create(
                model=os.getenv("GROQ_MODEL"),
                messages=self.history,
                tools=tools,
                tool_choice="auto"
            )
            return res.choices[0].message.model_dump()
        elif self.provider == "ollama":
            res = ollama.chat(
                model=os.getenv("OLLAMA_MODEL"),
                messages=self.history,
                tools=tools
            )
            return res["message"]
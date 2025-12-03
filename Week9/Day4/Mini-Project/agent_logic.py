import os
import sys
import json
import logging
import asyncio
from typing import List, Dict, Any, AsyncGenerator

from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from contextlib import AsyncExitStack

from groq import Groq, BadRequestError
import ollama

load_dotenv()

# --- DIAGNOSTIC ---
print("--- DÉBUT DIAGNOSTIC ---")
token = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")
if not token:
    print("ERREUR : Token GitHub manquant.")
else:
    print(f"Token GitHub trouvé.")

base_dir = os.getenv("ALLOWED_DIR", "./workspace")
abs_path = os.path.abspath(base_dir)
if not os.path.exists(abs_path):
    os.makedirs(abs_path, exist_ok=True)
print(f"Workspace : {abs_path}")
print("--- FIN DIAGNOSTIC ---")


class MCPAgent:
    def __init__(self):
        self.provider = os.getenv("LLM_PROVIDER", "groq")
        
        # Prompt Système strict
        system_prompt = (
            "You are a Senior Tech Lead Agent. You have access to 3 servers: "
            "1. GitHub (Fetch data), 2. Filesystem (Save reports), 3. SmartSentinel (Analyze risk). "
            "CRITICAL RULES:"
            "1. Always fetch real data from GitHub first."
            "2. Send that data to SmartSentinel tools to get analysis."
            "3. Only use Filesystem to save the FINAL result."
            "4. Do NOT simulate tool outputs. Wait for real execution."
            "5. Use standard JSON for tool calls."
        )
        
        self.history = [{"role": "system", "content": system_prompt}]
        
        if self.provider == "groq":
            self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    async def run_process(self, user_prompt: str) -> AsyncGenerator[Dict, None]:
        self.history.append({"role": "user", "content": user_prompt})

        # --- 1. CONFIGURATION DES 3 SERVEURS ---
        
        # Serveur A : GitHub (Node.js)
        github_params = StdioServerParameters(
            command="npx",
            args=["@modelcontextprotocol/server-github"],
            env={**os.environ}
        )
        
        # Serveur B : Filesystem (Node.js)
        fs_params = StdioServerParameters(
            command="npx",
            args=["@modelcontextprotocol/server-filesystem", abs_path],
            env={**os.environ}
        )

        # Serveur C : VOTRE Serveur (Python)
        # On utilise sys.executable pour s'assurer qu'il utilise le même Python (venv)
        my_server_params = StdioServerParameters(
            command=sys.executable,
            args=["my_server.py"],
            env={**os.environ}
        )

        try:
            async with AsyncExitStack() as stack:
                yield {"type": "log", "content": "Connexion aux 3 serveurs (GitHub, FS, Sentinel)..."}
                
                # Connexion GitHub
                gh_read, gh_write = await stack.enter_async_context(stdio_client(github_params))
                gh_session = await stack.enter_async_context(ClientSession(gh_read, gh_write))
                await gh_session.initialize()
                
                # Connexion Filesystem
                fs_read, fs_write = await stack.enter_async_context(stdio_client(fs_params))
                fs_session = await stack.enter_async_context(ClientSession(fs_read, fs_write))
                await fs_session.initialize()

                # Connexion SmartSentinel (VOTRE SERVEUR)
                sentinel_read, sentinel_write = await stack.enter_async_context(stdio_client(my_server_params))
                sentinel_session = await stack.enter_async_context(ClientSession(sentinel_read, sentinel_write))
                await sentinel_session.initialize()

                yield {"type": "log", "content": "Les 3 serveurs sont connectés !"}

                # --- AGRÉGATION DES OUTILS ---
                tools = []
                tool_map = {}

                async def register_tools(session, source_name):
                    t_list = await session.list_tools()
                    for t in t_list.tools:
                        tools.append({
                            "type": "function",
                            "function": {
                                "name": t.name,
                                "description": t.description,
                                "parameters": t.inputSchema
                            }
                        })
                        tool_map[t.name] = session
                        # Log pour vérifier que vos outils sont bien là
                        if source_name == "Sentinel":
                            print(f"   Outil chargé : {t.name}")

                await register_tools(gh_session, "GitHub")
                await register_tools(fs_session, "Filesystem")
                await register_tools(sentinel_session, "Sentinel")

                yield {"type": "log", "content": f"  Total outils disponibles : {len(tools)}"}

                # --- BOUCLE DE RAISONNEMENT ---
                while True:
                    try:
                        raw_response = self._call_llm(tools)
                    except BadRequestError as e:
                        if "tool_use_failed" in str(e):
                            self.history.append({"role": "user", "content": "Error: Invalid Format. Use JSON."})
                            continue
                        raise e

                    # Nettoyage Groq
                    clean_response = {
                        "role": raw_response["role"],
                        "content": raw_response.get("content")
                    }
                    if raw_response.get("tool_calls"):
                        clean_response["tool_calls"] = raw_response["tool_calls"]
                    
                    self.history.append(clean_response)
                    
                    if not clean_response.get("tool_calls"):
                        yield {"type": "answer", "content": clean_response["content"]}
                        break

                    # Exécution des outils
                    for tool_call in clean_response["tool_calls"]:
                        fn_name = tool_call["function"]["name"]
                        fn_args = json.loads(tool_call["function"]["arguments"])
                        
                        yield {"type": "log", "content": f" Exécution : **{fn_name}**"}
                        
                        try:
                            if fn_name in tool_map:
                                # Appel via MCP
                                mcp_res = await tool_map[fn_name].call_tool(fn_name, arguments=fn_args)
                                result = mcp_res.content[0].text
                            else:
                                result = "Error: Tool not found."
                        except Exception as e:
                            result = f"Error: {str(e)}"
                            yield {"type": "log", "content": f" Erreur : {result}"}

                        self.history.append({
                            "role": "tool",
                            "tool_call_id": tool_call["id"],
                            "name": fn_name,
                            "content": str(result)
                        })

        except Exception as e:
            print(f" ERREUR AGENT : {e}")
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
            res = ollama.chat(model=os.getenv("OLLAMA_MODEL"), messages=self.history, tools=tools)
            return res["message"]
import streamlit as st
import asyncio
import nest_asyncio
import os
from dotenv import load_dotenv

# Patch pour asyncio dans Streamlit
nest_asyncio.apply()
load_dotenv()

st.set_page_config(page_title="MCP Commander", page_icon="🤖")

# --- SIDEBAR CONFIGURATION (Demandé par le checker) ---
st.sidebar.title("⚙️ Configuration")
provider_option = st.sidebar.selectbox(
    "LLM Provider",
    ["groq", "ollama"],
    index=0
)

# Choix du modèle dynamique
if provider_option == "groq":
    model_option = st.sidebar.text_input("Model Name", value="llama-3.1-70b-versatile")
    api_key_status = "✅ Set" if os.getenv("GROQ_API_KEY") else "❌ Missing"
    st.sidebar.caption(f"API Key: {api_key_status}")
else:
    model_option = st.sidebar.text_input("Model Name", value="llama3.2")
    st.sidebar.caption("Ensure Ollama is running locally")

# Import de la logique après la config
try:
    from agent_logic import MCPAgent
except ImportError:
    st.error("Could not import agent_logic.py. Check file structure.")
    st.stop()

# --- INTERFACE PRINCIPALE ---
st.title("🤖 MCP Agentic Application")
st.markdown(f"**Backend:** {provider_option.upper()} | **Tools:** GitHub, Filesystem, Local Analysis")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter your request..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Instanciation de l'agent avec les options de la Sidebar
        try:
            agent = MCPAgent(provider=provider_option, model=model_option)
            
            message_placeholder = st.empty()
            status_container = st.status("Agent Orchestration...", expanded=True)
            
            async def run_process():
                final_text = ""
                async for update in agent.run_process(prompt):
                    if update["type"] == "log":
                        status_container.write(f"🔹 {update['content']}")
                    elif update["type"] == "error":
                        status_container.error(update["content"])
                    elif update["type"] == "answer":
                        final_text = update["content"]
                return final_text

            response = asyncio.run(run_process())
            
            if response:
                status_container.update(label="Process Completed", state="complete", expanded=False)
                message_placeholder.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            else:
                status_container.update(label="Process Failed", state="error")
                
        except Exception as e:
            st.error(f"Application Error: {e}")
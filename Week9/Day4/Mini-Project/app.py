import streamlit as st
import asyncio
import nest_asyncio

# IMPORTANT : Appliquer nest_asyncio tout de suite
nest_asyncio.apply()

# Import de la classe agent
from agent_logic import MCPAgent

st.set_page_config(page_title="MCP Commander", page_icon="🤖")

st.title("🤖 MCP Research Commander")
st.markdown("""
Cet agent intègre **GitHub**, **Filesystem**, et une **Analyse Locale**.
""")

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Ex: 'Check repo modelcontextprotocol/python-sdk issues'"):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Agent Execution
    with st.chat_message("assistant"):
        agent = MCPAgent()
        message_placeholder = st.empty()
        full_response = ""
        
        # Container pour les logs des outils
        status_container = st.status("L'agent travaille...", expanded=True)
        
        async def run_agent():
            response_text = ""
            async for update in agent.run_process(prompt):
                if update["type"] == "log":
                    status_container.write(update["content"])
                elif update["type"] == "answer":
                    response_text = update["content"]
            return response_text

        # Run Async Logic
        try:
            final_answer = asyncio.run(run_agent())
            status_container.update(label="Tâche terminée !", state="complete", expanded=False)
            message_placeholder.markdown(final_answer)
            
            st.session_state.messages.append({"role": "assistant", "content": final_answer})
        except Exception as e:
            status_container.update(label="Erreur", state="error")
            st.error(f"Une erreur est survenue : {e}")
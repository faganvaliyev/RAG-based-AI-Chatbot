import streamlit as st
from services.api_client import stream_chat_api

st.title("RAG AI Chatbot (LLM-only Streaming)")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Ask something...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Placeholder in UI for streaming response
    message_placeholder = st.empty()
    answer = ""

    for token in stream_chat_api(user_input):
        answer += token
        message_placeholder.markdown(f"**assistant**: {answer}")

    st.session_state.messages.append({"role": "assistant", "content": answer})

# Display previous messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**user**: {msg['content']}")
    else:
        st.markdown(f"**assistant**: {msg['content']}")


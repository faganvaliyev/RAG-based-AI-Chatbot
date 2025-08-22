import streamlit as st
from services.api_client import chat_api
from services.chat_service import init_session, create_chat, delete_chat, _append_message_to_session, get_current_chat
import PyPDF2
import docx
import pandas as pd


# Initialize session state
init_session()


st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)


st.title("🤖 AI Chatbot")


# Sidebar 
with st.sidebar:
    st.header("📂 File Upload")
    uploaded_files = st.file_uploader("Upload files", type=["txt", "pdf", "csv", "docx"], accept_multiple_files=True)
   
    if uploaded_files:
        st.session_state["files"] = []
        for uploaded_file in uploaded_files:
            file_text = ""
            if uploaded_file.type == "text/plain":
                file_text = uploaded_file.read().decode("utf-8")
            elif uploaded_file.type == "application/pdf":
                pdf_reader = PyPDF2.PdfReader(uploaded_file)
                file_text = "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
            elif uploaded_file.type == "text/csv":
                df = pd.read_csv(uploaded_file)
                file_text = df.to_string()
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                doc = docx.Document(uploaded_file)
                file_text = "\n".join([para.text for para in doc.paragraphs])
           
            st.session_state["files"].append({"name": uploaded_file.name, "content": file_text[:2000]})  # limit size
            st.success(f"Loaded {uploaded_file.name}")


    st.divider()
    st.header("⚙️ Chat Controls")


    # Chat history
    chat_history_menu = [
        f"{chat['chat_name']}_::_{chat['chat_id']}"
        for chat in st.session_state["history_chats"]
    ]
    chat_history_menu = chat_history_menu[:50][::-1]


    if chat_history_menu:
        current_chat = st.radio(
            "History Chats",
            options=chat_history_menu,
            index=st.session_state["current_chat_index"],
            key="current_chat",
            format_func=lambda x: x.split("_::_")[0] + '...'
        )
        if current_chat:
            st.session_state["current_chat_id"] = current_chat.split("_::_")[1]
            st.session_state["messages"] = get_current_chat(st.session_state["current_chat_id"])


    # Buttons
    c1, c2 = st.columns(2)
    if c1.button("New Chat", use_container_width=True):
        create_chat()
        st.rerun()
    if c2.button("Delete Chat", use_container_width=True):
        delete_chat(st.session_state.get("current_chat_id"))
        st.rerun()


    st.divider()
    st.subheader("⚙️ Model Settings")
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
    max_tokens = st.slider("Max Tokens", 256, 2048, 1024, 64)


# Chat UI 
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# User input 
if prompt := st.chat_input("Ask something..."):
    # If files uploaded, prepend their content to user query
    context = ""
    if "files" in st.session_state and st.session_state["files"]:
        file_texts = "\n\n".join([f"--- {f['name']} ---\n{f['content']}" for f in st.session_state["files"]])
        context = f"Here are the uploaded files:\n{file_texts}\n\nUser Question: {prompt}"
    else:
        context = prompt


    # Save user message
    user_msg = {"role": "user", "content": prompt}
    _append_message_to_session(user_msg)
    with st.chat_message("user"):
        st.markdown(prompt)


    # Stream assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        answer = ""


        answer = chat_api(context, temperature=temperature, max_tokens=max_tokens)
        message_placeholder.markdown(answer)  


    assistant_msg = {"role": "assistant", "content": answer}
    _append_message_to_session(assistant_msg)

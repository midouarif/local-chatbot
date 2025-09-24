import streamlit as st
from langchain_ollama import ChatOllama

st.set_page_config(page_title="DeepSeek Chatbot", layout="centered")
st.title("💬 DeepSeek-R1 Chatbot")
st.write("Hello Midou, welcome to your own chatbot!")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize LLM client only once
llm = ChatOllama(
    model="deepseek-r1:1.5b",
    base_url="http://localhost:11434"
)

def generate_response(input_text):
    with st.spinner("Thinking..."):
        response = llm.invoke(input_text)
    return response.content

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

# User input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    # Generate assistant response
    response = generate_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").markdown(response)

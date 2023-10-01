import streamlit as st
from streamlit_chat import message
from utils import get_initial_message, get_chatgpt_response, update_chat
import os
from dotenv import load_dotenv

load_dotenv()
import openai

openai.api_key = os.getenv("OPENAI_API_KEY1")

st.title("Codebot: by ChatGPT and Streamlit")
st.subheader("Auto Code Mode")

# Dropdown model selection code
model = st.selectbox("Select a model",
                     ("gpt-3.5-turbo", "gpt-3.5-turbo-0301")
                     )

# Session created to save past conversation
if 'chatgpt_reply' not in st.session_state:
    st.session_state['chatgpt_reply'] = []
if 'user_reply' not in st.session_state:
    st.session_state['user_reply'] = []

# User input taken
query = st.text_input("Query: ", key="input")

if 'messages' not in st.session_state:
    st.session_state['messages'] = get_initial_message()

# Chat Completion 
if query:
    with st.spinner("generating..."):
        messages = st.session_state['messages']
        messages = update_chat(messages, "user", query)
        prompt = get_chatgpt_response(messages, model)
        messages = update_chat(messages, "assistant", prompt)
        st.session_state.user_reply.append(query)
        st.session_state.chatgpt_reply.append(prompt)

# Display on the user interface
if st.session_state['chatgpt_reply']:

    for i in range(len(st.session_state['chatgpt_reply']) - 1, -1, -1):
        message(st.session_state['user_reply'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["chatgpt_reply"][i], key=str(i))

    #
    with st.expander("Show Messages"):
        st.write(messages)

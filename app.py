import streamlit as st
from streamlit_chat import message

import google.generativeai as palm


def clear_chat():
    st.session_state.messages = [{"role": "assistant", "content": "Say something to get started!"}]


with st.sidebar:
    palm_api_key = st.text_input('PaLM API Key', key='palm_api_key')
    "Don't have API Key? [Join the waitlist](https://developers.generativeai.google/products/palm)"
    "[View the source code](https://github.com/abdibrokhim/PaLM2-Tutorial)"


st.title("PaLM Tutorial")


if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Say something to get started!"}]


with st.form("chat_input", clear_on_submit=True):
    a, b = st.columns([4, 1])

    user_prompt = a.text_input(
        label="Your message:",
        placeholder="Type something...",
        label_visibility="collapsed",
    )

    b.form_submit_button("Send", use_container_width=True)


for msg in st.session_state.messages:
    message(msg["content"], is_user=msg["role"] == "user")


if user_prompt and not palm_api_key:
    st.info("Please add your PaLM API key to continue.")
    

if user_prompt and palm_api_key:

    print('user_prompt: ', user_prompt)

    try:
        palm.configure(api_key=palm_api_key)
    except Exception as e:
        st.info("Please pass a valid API key")

    st.session_state.messages.append({"role": "user", "content": user_prompt})
    
    message(user_prompt, is_user=True)

    response = palm.chat(messages=[user_prompt])

    msg = {"role": "assistant", "content": response.last}

    print('st.session_state.messages: ', st.session_state.messages)

    st.session_state.messages.append(msg)

    print('msg.content: ', msg["content"])

    message(msg["content"])


if len(st.session_state.messages) > 1:
    st.button('Clear Chat', on_click=clear_chat)

# frontend.py
import streamlit as st
import requests

st.title("Chat with GPT via FastAPI")

user_input = st.text_input("Ask something:")

if user_input:
    try:
        res = requests.post("http://localhost:8000/chat", json={"prompt": user_input})
        if res.status_code == 200 and "response" in res.json():
            st.success(res.json()["response"])
        else:
            st.error(res.json().get("error", "Something went wrong."))
    except Exception as e:
        st.error(f"Request failed: {e}")

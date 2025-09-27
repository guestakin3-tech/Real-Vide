# AkinAI - Your Personal ChatGPT Clone
# Created by Akin Sokpah
# Run with: streamlit run akina_ai.py

import streamlit as st
import openai
import os
from datetime import datetime

# ==============================
# 🔒 SECURITY: Load API Key Safely
# ==============================
# Option 1: Use Streamlit Secrets (recommended for deployment)
# Option 2: Use environment variable (for local testing)
# NEVER hardcode your key in the file!

if "OPENAI_API_KEY" in st.secrets:
    openai.api_key = st.secrets["OPENAI_API_KEY"]
else:
    # For local testing: set env var or replace with your key temporarily
    openai.api_key = os.getenv("OPENAI_API_KEY", "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")

# ==============================
# 🧠 AI Chat Function
# ==============================
def get_ai_response(messages):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Free & powerful
            messages=messages,
            temperature=0.7,
            max_tokens=500
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        if "authentication" in str(e).lower():
            return "❌ Error: Invalid or missing OpenAI API key. Please configure it properly."
        return f"❌ AI Error: {str(e)}"

# ==============================
# 🌐 Streamlit UI
# ==============================
st.set_page_config(
    page_title="AkinAI by Akin Sokpah",
    page_icon="🤖",
    layout="centered"
)

# Header
st.title("🤖 AkinAI")
st.caption("Your personal AI assistant — built by **Akin Sokpah**")
st.markdown("Ask anything: explain science, write code, brainstorm ideas, or just chat!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm AkinAI. How can I help you today?"}
    ]

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_ai_response(st.session_state.messages)
        st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# Footer
st.divider()
st.caption("Powered by OpenAI • Created by Akin Sokpah • Not affiliated with ChatGPT or Google")

import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Page configuration
st.set_page_config(page_title="Gen AI App", page_icon="🤖", layout="wide")

# Sidebar for settings
with st.sidebar:
    st.title("AI Settings")
    model_choice = st.selectbox("Model", ["gemini-2.0-flash", "gemini-pro"])
    temperature = st.slider("Creativity", 0.0, 1.0, 0.7)

# Main interface
st.title("Generative AI App")
col1, col2 = st.columns([1, 2])
with col1:
    prompt = st.text_area("Enter your AI prompt", height=150)
    if st.button("Generate"):
        if prompt:
            with st.spinner("Generating..."):
                model = genai.GenerativeModel(model_choice)
                try:
                    response = model.generate_content(prompt, generation_config={"temperature": temperature})
                    st.session_state["last_response"] = response.text
                except Exception as e:
                    st.error(f"Error: {str(e)}")
with col2:
    st.write("**AI Response:**")
    if "last_response" in st.session_state:
        st.markdown(st.session_state["last_response"])
    if st.button("Regenerate"):
        if prompt:
            with st.spinner("Regenerating..."):
                response = model.generate_content(prompt)
                st.session_state["last_response"] = response.text

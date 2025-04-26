import streamlit as st
import google.generativeai as genai
import time

st.header("Hello there! I am Code AI.")
st.write("I am your intelligent coding assistant. Whether you're building a website, debugging Python, or exploring new programming languages, I generate clean, efficient code tailored to your needs.")
st.title("_Code-AI:_")

api_key = "AIzaSyCxFbvsEa5N0LO_af9O0sVGLtRJspPsUvw"
genai.configure(api_key=api_key)

# Extra modification...
p1, p2, p3, p4 = st.columns(4)

with p1:
    st.info("🔧 Generate Python scripts for automation")

with p2:
    st.info("🌐 Create HTML, CSS, and JS code for websites")

with p3:
    st.info("🧠 Build AI/ML model templates in Python")

with p4:
    st.info("🐛 Debug and optimize your existing code")

# Main section
prompt = st.chat_input("Enter your prompt here...")
if prompt:
    st.chat_message("human").write(prompt)
    with st.spinner("Generating response"):
        time.sleep(3.5)
    model = genai.GenerativeModel(model_name='tunedModels/codeai-9oln2fiw1c3c')
    response = model.generate_content(prompt)
    st.chat_message("ai").write(response.text)
import streamlit as st
import google.generativeai as genai
import time

st.header("Hello there! I am Resume-Builder.")
st.write("I'm your AI-powered assistant for crafting professional, modern, and job-winning resumes. Just tell me your details or job field and I'll handle the rest.")
st.title("_Resume-Mate-AI:_")

api_key = ""
genai.configure(api_key=api_key)
# Extra Modification...
p1, p2, p3, p4 = st.columns(4)

with p1:
    st.info("📄 Generate tailored resumes for any job role")

with p2:
    st.info("🎯 Highlight your skills and achievements")

with p3:
    st.info("🧑‍💼 Create resumes for freshers and professionals")

with p4:
    st.info("🌍 Support for international resume formats")

# Main section...
prompt = st.chat_input("Enter your prompt here...")
if prompt:
    st.chat_message("human").write(prompt)
    with st.spinner("Generating response"):
        time.sleep(3.5)
    model = genai.GenerativeModel(model_name='tunedModels/codeai-9oln2fiw1c3c')
    response = model.generate_content(prompt)
    st.chat_message("ai").write(response.text)
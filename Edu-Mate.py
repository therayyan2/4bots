import streamlit as st
import time
import google.generativeai as genai

st.header("Hello there! I am Your StudyBuddy-AI.")
st.write("I'm your personal AI tutor, ready to help with homework, explain tough concepts, and make learning fun across all subjects and difficulty levels.")
st.title("_Study-Budy:_")

api_key = ""
genai.configure(api_key=api_key)
# Extra modification...
p1, p2, p3, p4 = st.columns(4)

with p1:
    st.info("📘 Solve homework and assignments")

with p2:
    st.info("🧠 Explain math, science, and more")

with p3:
    st.info("🎓 Prepare for quizzes and exams")

with p4:
    st.info("🌟 Learn concepts step-by-step")

# Main section...
prompt = st.chat_input("Enter your prompt here...")
if prompt:
    st.chat_message("human").write(prompt)
    with st.spinner("Generating response"):
        time.sleep(3.5)
    model = genai.GenerativeModel(model_name='tunedModels/codeai-9oln2fiw1c3c')
    response = model.generate_content(prompt)
    st.chat_message("ai").write(response.text)
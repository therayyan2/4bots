import streamlit as st
import time
import google.generativeai as genai

st.header("Hello there! I am Story-Forge.")
st.write("I'm your creative storytelling companion. Whether it's fantasy, sci-fi, horror, or a bedtime tale, I bring your ideas to life with immersive and imaginative stories.")
st.title("_Story-Forge:_")

api_key = ""
genai.configure(api_key=api_key)
# Extra modification...
p1, p2, p3, p4 = st.columns(4)

with p1:
    st.info("📚 Write short stories or full-length tales")

with p2:
    st.info("🌌 Create fantasy, sci-fi, or horror stories")

with p3:
    st.info("👧 Generate children’s bedtime stories")

with p4:
    st.info("✍️ Continue or rewrite existing story drafts")

# Main section...
prompt = st.chat_input("Enter your prompt here...")
if prompt:
    st.chat_message("human").write(prompt)
    with st.spinner("Generating response"):
        time.sleep(3.5)
    model = genai.GenerativeModel(model_name='tunedModels/codeai-9oln2fiw1c3c')
    response = model.generate_content(prompt)
    st.chat_message("ai").write(response.text)
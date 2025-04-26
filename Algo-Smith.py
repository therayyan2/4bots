# Main general bot code..
import streamlit as st
import google.generativeai as genai
import time

st.set_page_config("Orion-AI")

st.header("Hey there! how can i help with...")
st.title("_Orion-AI:_")
st.sidebar.info("🤖 Explore Bots 👆")
api_key = "AIzaSyDqp_kA9gJGYALqSdjStTceD0HdWRAelhE"
genai.configure(api_key=api_key)

# Extra Modification...
pre1,pre2,pre3,pre4 = st.columns(4)

with pre1:
    st.info("🌀 If I only have 6 months to master data science, what’s the best learning path?")
    
with pre2:
    st.info("📝 Give me a structured breakdown of the history of artificial intelligence with key milestones.")

with pre3:
    st.info("📖 Write a short realistic story where AI and humans must unite to stop an alien invasion.")

with pre4:
    st.info("🌠Tell me how cryptocurrency works and whether it’s a reliable investment.")


# Main Code...
prompt = st.chat_input("Enter your prompt...")
if prompt:
    st.chat_message("human").write(prompt)
    with st.spinner("Generating response"):
        time.sleep(3.5)
    model = genai.GenerativeModel(model_name='gemini-1.5-flash')
    response = model.generate_content(prompt)
    st.chat_message("ai").write(response.text)
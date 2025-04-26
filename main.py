import streamlit as st

st.title("⚡Explore Bots⚡")

st.write("These bots have different features based on their roles. Explore now to check how these bots actually work.")

algo, career, code, Edu, story = st.columns(5)

with algo:
    st.subheader("")
    st.write("")
    st.info("Orion Helps in understanding algorithms.")
    st.page_link("pages/Algo-Smith.py", label="Explore Orion")

with career:
    st.subheader("")
    st.write("")
    st.info("Rezoom Helps to build resumes.")
    st.page_link("pages/Career-Crafter.py", label="Explore Rezoom")

with code:
    st.subheader("")
    st.write("")
    st.info("Code-AI Helps in writing and fixing code.")
    st.page_link("pages/Code-AI.py", label="Explore Code-AI")

with Edu:
    st.subheader("")
    st.write("")
    st.info("Study-Mentor Helps to solves problems.")
    st.page_link("pages/Edu-Mate.py", label="Explore Studo")

with story:
    st.subheader("")
    st.write("")
    st.info("Forge Helps in Generating creative stories.")
    st.page_link("pages/Story-Forge.py", label="Explore Forge")
    
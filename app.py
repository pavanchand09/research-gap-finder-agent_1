import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="Research Gap Finder",
    page_icon="🔍",
    layout="wide"
)

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

st.title("🔍 AI Research Gap Finder")

st.write("Welcome to the AI Research Gap Finder.")

topic = st.text_input("Enter a Research Topic")

if st.button("Test Groq"):

    if topic == "":
        st.warning("Please enter a topic.")
    else:

        with st.spinner("Connecting to Groq..."):

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": f"Give one sentence about {topic}."
                    }
                ]
            )

        st.success("Connected Successfully!")

        st.write(response.choices[0].message.content)

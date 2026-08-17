import streamlit as st
from groq import Groq
from utils import search_papers
from prompts import research_gap_prompt
from report import download_report

st.set_page_config(
    page_title="Research Gap Finder",
    page_icon="🔍",
    layout="wide"
)

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("🔍 AI Research Gap Finder")

topic = st.text_input("Enter Research Topic")

if st.button("Analyze"):

    if not topic:
        st.warning("Please enter a research topic.")
        st.stop()

    with st.spinner("Searching research papers..."):
        papers = search_papers(topic)

    if not papers:
        st.error("No papers found or the API request failed. Check the Streamlit logs.")
        st.stop()

    st.header("Research Papers")

    paper_text = ""

    for i, paper in enumerate(papers, 1):

        title = paper.get("title", "No Title")
        abstract = paper.get("abstract", "No Abstract")
        year = paper.get("year", "N/A")

        st.subheader(f"{i}. {title}")
        st.write(f"**Year:** {year}")
        st.write(abstract)
        st.divider()

        paper_text += f"""
Title: {title}

Year: {year}

Abstract:
{abstract}

"""

    prompt = research_gap_prompt(topic, paper_text)

    with st.spinner("Finding Research Gaps..."):

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

    analysis = response.choices[0].message.content

    st.header("Research Gap Analysis")

    st.markdown(analysis)

    download_report(topic, analysis)

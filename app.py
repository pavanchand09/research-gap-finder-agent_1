from report import download_report
from prompts import research_gap_prompt
from utils import search_papers
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

if st.button("Search Papers"):

    if topic == "":
        st.warning("Please enter a topic.")
    else:

        with st.spinner("Searching Papers..."):

            papers = search_papers(topic)

        if len(papers) == 0:
            st.error("No papers found.")
        else:

            st.success(f"{len(papers)} papers found.")

            for i, paper in enumerate(papers, 1):

                st.subheader(f"{i}. {paper.get('title','No Title')}")

                st.write("**Year:**", paper.get("year", "N/A"))

                st.write("**Citations:**", paper.get("citationCount", 0))

                authors = paper.get("authors", [])

                if authors:
                    names = ", ".join(
                        [author["name"] for author in authors]
                    )
                    st.write("**Authors:**", names)

                st.write("**Abstract:**")

                st.write(
                    paper.get(
                        "abstract",
                        "No abstract available."
                    )
                )

                st.divider()
    paper_text = ""

for paper in papers:

    title = paper.get("title", "")

    abstract = paper.get("abstract", "")

    year = paper.get("year", "")

    paper_text += f"""

Title: {title}

Year: {year}

Abstract:
{abstract}

"""
prompt = research_gap_prompt(topic, paper_text)
with st.spinner("Analyzing Research Gaps..."):

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

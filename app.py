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

st.success("✅ App Started Successfully")

topic = st.text_input("Enter Research Topic")

if st.button("Analyze"):

    if topic.strip() == "":
        st.warning("Please enter a research topic.")
        st.stop()

    st.write("## Step 1: User entered topic")
    st.write(topic)

    # ---------------- SEARCH PAPERS ---------------- #

    try:

        with st.spinner("Searching research papers..."):

            papers = search_papers(topic)

        st.success("✅ Step 2: search_papers() completed")

        st.write("Number of papers found:", len(papers))

        st.json(papers)

    except Exception as e:

        st.error("❌ Error while searching papers")

        st.exception(e)

        st.stop()

    if len(papers) == 0:

        st.error("No papers found.")

        st.stop()

    # ---------------- DISPLAY PAPERS ---------------- #

    st.header("Research Papers")

    paper_text = ""

    for i, paper in enumerate(papers, start=1):

        title = paper.get("title", "No Title")

        abstract = paper.get("abstract", "No Abstract")

        year = paper.get("year", "N/A")

        st.subheader(f"{i}. {title}")

        st.write("Year:", year)

        st.write(abstract)

        st.divider()

        paper_text += f"""

Title: {title}

Year: {year}

Abstract:
{abstract}

"""

    st.success("✅ Step 3: Papers displayed")

    # ---------------- CREATE PROMPT ---------------- #

    prompt = research_gap_prompt(topic, paper_text)

    st.success("✅ Step 4: Prompt Created")

    # ---------------- GROQ ---------------- #

    try:

        with st.spinner("Finding Research Gaps..."):

            response = client.chat.completions.create(

                model="openai/gpt-oss-120b",

                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]

            )

        st.success("✅ Step 5: Groq Response Received")

    except Exception as e:

        st.error("❌ Groq API Error")

        st.exception(e)

        st.stop()

    analysis = response.choices[0].message.content

    st.header("Research Gap Analysis")

    st.markdown(analysis)

    download_report(topic, analysis)

    st.success("✅ Finished Successfully")

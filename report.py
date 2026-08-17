import streamlit as st

def download_report(topic, analysis):

    report = f"""
# Research Gap Analysis Report

## Research Topic

{topic}

---

{analysis}

---

Generated using AI Research Gap Finder Agent.
"""

    st.download_button(
        label="📥 Download Report",
        data=report,
        file_name="Research_Gap_Report.md",
        mime="text/markdown"
    )

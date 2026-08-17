def research_gap_prompt(topic, papers):
    return f"""
You are an expert research analyst and AI scientist.

Your task is to analyze the following research papers related to:

TOPIC:
{topic}

RESEARCH PAPERS:
{papers}

Perform the following tasks carefully.

1. Summarize each paper in 3-5 points.

2. Identify the common research trends.

3. Identify the algorithms, models, or techniques frequently used.

4. List the strengths of the existing research.

5. List the limitations of the existing research.

6. Find the research gaps that are not addressed by these papers.

7. Suggest at least 5 novel research ideas based on those gaps.

8. Suggest future research directions.

9. Finally, provide an overall conclusion.

Format the response using the following headings:

# Paper Summaries

# Common Trends

# Techniques Used

# Strengths

# Limitations

# Research Gaps

# Novel Project Ideas

# Future Scope

# Conclusion
"""

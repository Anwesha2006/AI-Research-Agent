from app.schemas import ResearchRequest
from app.services.search import search
from app.services.llm import model


def research_topic(request: ResearchRequest):

    # 1. Search the web using Tavily
    search_results = search(
        request.topic,
        max_results=request.max_sources
    )

    # 2. Prepare the search results for Gemini
    sources_text = ""

    for index, result in enumerate(search_results["results"], start=1):
        title = result.get("title", "")
        url = result.get("url", "")
        content = result.get("content", "")

        sources_text += f"""
SOURCE {index}
Title: {title}
URL: {url}
Content:
{content}

"""

    # 3. Create the prompt for Gemini
    prompt = f"""
You are an AI research assistant.

Research topic:
{request.topic}

Research depth:
{request.depth}

Analyze the following web sources and produce a reliable research analysis.

IMPORTANT RULES:
- Base your analysis on the provided sources.
- Do not invent facts or sources.
- Clearly identify the important findings.
- Mention limitations or conflicting information when relevant.
- Do not claim something is true if the provided sources do not support it.

WEB SOURCES:
{sources_text}

Provide:

1. A concise summary
2. Key findings
3. Detailed analysis
4. Limitations
5. A conclusion
"""

    # 4. Send the prompt to Gemini
    response = model.invoke(prompt)

    # 5. Return the research result
    return {
        "topic": request.topic,
        "sources": search_results["results"],
        "analysis": response.content
    }



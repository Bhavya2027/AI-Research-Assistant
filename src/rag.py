import os

from langchain_core.prompts import PromptTemplate
from src.web_search import search_web


def extract_text(response):
    """
    Convert Gemini/LangChain response into plain text.
    """

    if hasattr(response, "content"):
        content = response.content
    else:
        content = response

    if isinstance(content, str):
        return content.strip()

    if isinstance(content, list):

        text = ""

        for item in content:

            if isinstance(item, dict):
                if item.get("type") == "text":
                    text += item.get("text", "")

            elif hasattr(item, "text"):
                text += item.text

            else:
                text += str(item)

        return text.strip()

    return str(content).strip()


def answer_question(
    question,
    retriever,
    llm,
    chat_history,
    pdf_name=None,
):
    """
    Answer using:

    - Multiple PDFs
    - Web Search
    - Conversation History
    """

    # -----------------------------
    # Retrieve Relevant Chunks
    # -----------------------------
    docs = retriever.invoke(question)

    pdf_context = "\n\n".join(
        doc.page_content for doc in docs
    )

    # -----------------------------
    # Sources
    # -----------------------------
    sources = []

    pdf_sources = set()

    for doc in docs:

        source = doc.metadata.get("source")

        if source:
            pdf_sources.add(os.path.basename(source))

    if pdf_sources:

        for pdf in sorted(pdf_sources):
            sources.append(f"✓ {pdf}")

    # -----------------------------
    # Web Search
    # -----------------------------
    try:

        web_context = search_web(question)

        if (
            web_context
            and web_context != "No web results available."
        ):
            sources.append("✓ DuckDuckGo Search")

    except Exception:

        web_context = "No web results available."

    # -----------------------------
    # Combined Context
    # -----------------------------
    context = f"""
PDF Information

{pdf_context}

--------------------------------

Web Information

{web_context}
"""

    # -----------------------------
    # Chat History
    # -----------------------------
    history = ""

    for user, assistant in chat_history:

        history += f"""

User:
{user}

Assistant:
{assistant}

"""

    # -----------------------------
    # Prompt
    # -----------------------------
    prompt = PromptTemplate(
        input_variables=[
            "history",
            "context",
            "question",
        ],
        template="""
You are an AI Research Assistant.

Answer the user's question using the provided context.

Rules:

1. Prefer PDF information whenever available.
2. Use web search only if needed.
3. Use conversation history if relevant.
4. If the answer is not found in the PDFs, use web search.
5. Give clear and well-structured answers.
6. Do not mention whether the information came from PDFs or the web unless asked.

--------------------------------

Conversation History

{history}

--------------------------------

Context

{context}

--------------------------------

Question

{question}

Answer:
""",
    )

    final_prompt = prompt.format(
        history=history,
        context=context,
        question=question,
    )

    # -----------------------------
    # LLM
    # -----------------------------
    response = llm.invoke(final_prompt)

    final_answer = extract_text(response)

    # -----------------------------
    # Sources
    # -----------------------------
    if sources:

        final_answer += "\n\n---\n\n"
        final_answer += "### Sources\n\n"

        for source in sources:
            final_answer += f"- {source}\n"

    return final_answer

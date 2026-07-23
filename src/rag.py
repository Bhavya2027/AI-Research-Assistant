from langchain_core.prompts import PromptTemplate
from src.web_search import search_web


def extract_text(response):
    """
    Convert Gemini/LangChain response into plain text.
    """

    # AIMessage
    if hasattr(response, "content"):
        content = response.content
    else:
        content = response

    # Already a string
    if isinstance(content, str):
        return content.strip()

    # Gemini sometimes returns a list
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

    # Fallback
    return str(content).strip()


def answer_question(
    question,
    retriever,
    llm,
    chat_history,
    pdf_name,
):
    """
    Answer using:
    - PDF
    - Web Search
    - Conversation History
    """

    # --------------------------------
    # Retrieve PDF context
    # --------------------------------
    docs = retriever.invoke(question)

    pdf_context = "\n\n".join(
        doc.page_content for doc in docs
    )

    # --------------------------------
    # Sources
    # --------------------------------
    sources = []

    if docs:
        sources.append(f"✓ PDF ({pdf_name})")

    # --------------------------------
    # Web Search
    # --------------------------------
    try:

        web_context = search_web(question)

        if (
            web_context
            and web_context != "No web results available."
        ):
            sources.append("✓ DuckDuckGo Search")

    except Exception:
        web_context = "No web results available."

    # --------------------------------
    # Combined Context
    # --------------------------------
    context = f"""
PDF Information:
{pdf_context}

--------------------------------

Web Information:
{web_context}
"""

    # --------------------------------
    # Chat History
    # --------------------------------
    history = ""

    for user, assistant in chat_history:

        history += f"""
User:
{user}

Assistant:
{assistant}

"""

    # --------------------------------
    # Prompt
    # --------------------------------
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
2. Use web search only to supplement the answer.
3. Use conversation history if relevant.
4. If the answer isn't in the PDF, use the web.
5. Respond in clear Markdown.
6. Do NOT mention that you are using PDF or web unless asked.

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

    # --------------------------------
    # LLM
    # --------------------------------
    response = llm.invoke(final_prompt)

    # --------------------------------
    # Extract clean text
    # --------------------------------
    final_answer = extract_text(response)

    # Debug (remove later)
    print("=" * 60)
    print("TYPE:", type(final_answer))
    print("=" * 60)
    print(final_answer[:300])
    print("=" * 60)

    # --------------------------------
    # Sources
    # --------------------------------
    if sources:

        final_answer += "\n\n---\n\n"
        final_answer += "### Sources\n\n"

        for source in sources:
            final_answer += f"- {source}\n"

    return final_answer
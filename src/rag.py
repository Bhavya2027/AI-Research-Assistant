def generate_answer(question, retrived_docs, llm):
    """
    Generate an answer using the retrived document
    """
    context = "\n\n".join(
        doc.page_content for doc in retrived_docs
    )
    prompt = f"""
    You are a helpful AI Research Assistant.

Answer ONLY using the information provided in the context.

If the answer is not present in the context, say:

"I couldn't find that information in the provided documents."

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content
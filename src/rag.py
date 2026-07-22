def generate_answer(question, retrieved_docs, llm):
    """
    Generate an answer using the retrieved documents.
    """

    context = "\n\n".join(
        doc.page_content for doc in retrieved_docs
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
import os

from src.loader import load_pdf
from src.splitter import split_documents
from src.embeddings import get_embedding_model
from src.vectordb import create_vector_db
from src.retriever import load_vector_db, get_retriever
from src.llm import get_llm
from src.rag import answer_question


def main():
    print("=" * 60)
    print("          AI Research Assistant")
    print("=" * 60)

    # Folder containing PDFs
    pdf_folder = "data/pdfs"

    # Load all PDFs
    print("\nLoading PDF(s)...")
    documents = load_pdf(pdf_folder)

    # Get PDF names for source citation
    pdf_files = [
        file
        for file in os.listdir(pdf_folder)
        if file.endswith(".pdf")
    ]

    pdf_name = ", ".join(pdf_files)

    # Split documents
    print("Splitting documents...")
    chunks = split_documents(documents)

    # Load embedding model
    print("Loading embedding model...")
    embedding_model = get_embedding_model()

    # Create vector database
    print("Creating vector database...")
    create_vector_db(chunks, embedding_model)

    # Load vector database
    print("Loading vector database...")
    vector_db = load_vector_db(embedding_model)

    # Create retriever
    print("Creating retriever...")
    retriever = get_retriever(vector_db)

    # Load LLM
    print("Loading LLM...")
    llm = get_llm()

    print("\nSystem Ready!")
    print("Type 'exit' to quit.\n")

    # Conversation history
    chat_history = []

    while True:

        query = input("Ask a question: ")

        if query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        try:

            answer = answer_question(
                query,
                retriever,
                llm,
                chat_history,
                pdf_name
            )

            print("\n" + "=" * 60)
            print(answer)
            print("=" * 60)

            # Save conversation
            chat_history.append(
                (
                    query,
                    answer
                )
            )

        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()
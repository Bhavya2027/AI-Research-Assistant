from src.loader import load_pdf
from src.splitter import split_documents
from src.embeddings import get_embedding_model
from src.vectordb import create_vector_db
from src.retriever import load_vector_db, get_retriever
from src.llm import get_llm
from src.rag import generate_answer


def main():

    print("=" * 50)
    print("      AI Research Assistant")
    print("=" * 50)

    # Load PDF
    pdf_path = "data/pdfs/AI.pdf"
    documents = load_pdf(pdf_path)

    # Split into chunks
    chunks = split_documents(documents)

    # Load embedding model
    embedding_model = get_embedding_model()

    # Create Vector Database
    create_vector_db(chunks, embedding_model)

    # Load Vector Database
    vector_db = load_vector_db(embedding_model)

    # Create Retriever
    retriever = get_retriever(vector_db)

    # Load LLM
    llm = get_llm()

    print("\nAI Research Assistant is Ready!")
    print("Type 'exit' to quit.\n")

    while True:

        query = input("Ask a Question: ")

        if query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        try:

            print("Searching documents...")

            retrieved_docs = retriever.invoke(query)

            print(f"Retrieved {len(retrieved_docs)} document(s).")

            answer = generate_answer(
                query,
                retrieved_docs,
                llm
            )

            print("\nAnswer:\n")
            print(answer)

        except Exception as e:

            print("\nERROR:")
            print(e)

        print("\n" + "-" * 60 + "\n")


if __name__ == "__main__":
    main()
import os
import shutil

from langchain_chroma import Chroma


def create_vector_db(chunks, embedding_model):
    """
    Create a fresh Chroma vector database.
    """

    if not chunks:
        raise ValueError(
            "No document chunks found. Please check your PDF loading and splitting."
        )

    print(f"Creating Vector DB with {len(chunks)} chunks...")

    # Delete old database
    if os.path.exists("database"):
        shutil.rmtree("database")

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="database"
    )

    print("Vector database created successfully.")

    return vector_db
from langchain_chroma import Chroma

def create_vector_db(chunks,embedding_model):
    """
    Creates a chroma vector database from document chunks
    """
    vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="database"
    )

    return vector_db
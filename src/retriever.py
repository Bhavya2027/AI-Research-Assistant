from langchain_chroma import Chroma

def load_vector_db(embedding_model):
    """
    Load the existing chroma database
    """
    vector_db = Chroma(
        persist_directory="database",
        embedding_function=embedding_model
    )

    return vector_db

def get_retriever(vector_db):
    """
    Create a retriever from the vector database
    """
    retriever = vector_db.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever
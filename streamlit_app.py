import os

import streamlit as st

from src.pdf_loader import load_pdfs
from src.splitter import split_documents
from src.embeddings import get_embedding_model
from src.vectordb import create_vector_db
from src.retriever import load_vector_db, get_retriever
from src.llm import get_llm
from src.rag import answer_question


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Research Assistant",
    layout="wide"
)

st.title("AI Research Assistant")


# -----------------------------
# Load Models Only Once
# -----------------------------
@st.cache_resource
def initialize():

    pdf_folder = "data/pdfs"

    # Load all PDFs
    documents = load_pdfs(pdf_folder)

    # Split into chunks
    chunks = split_documents(documents)

    # Embeddings
    embedding = get_embedding_model()

    # Create Vector Database
    create_vector_db(chunks, embedding)

    # Load Vector Database
    vector_db = load_vector_db(embedding)

    # Retriever
    retriever = get_retriever(vector_db)

    # LLM
    llm = get_llm()

    # PDF names for source citations
    pdf_files = [
        file
        for file in os.listdir(pdf_folder)
        if file.endswith(".pdf")
    ]

    pdf_name = ", ".join(pdf_files)

    return retriever, llm, pdf_name


retriever, llm, pdf_name = initialize()


# -----------------------------
# Conversation History
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []


# -----------------------------
# User Input
# -----------------------------
question = st.text_input(
    "Ask anything"
)


# -----------------------------
# Ask Button
# -----------------------------
if st.button("Ask"):

    if question:

        with st.spinner("Searching..."):

            answer = answer_question(
                question,
                retriever,
                llm,
                st.session_state.history,
                pdf_name
            )

        # Save Conversation
        st.session_state.history.append(
            (
                question,
                answer
            )
        )

        # Display Answer
        st.subheader("Answer")

        st.markdown(answer)


# -----------------------------
# Sidebar Conversation
# -----------------------------
with st.sidebar:

    st.header("Conversation")

    if st.session_state.history:

        for q, a in st.session_state.history:

            st.markdown(f"**You:** {q}")

            preview = a[:100]

            if len(a) > 100:
                preview += "..."

            st.markdown(f"**AI:** {preview}")

            st.divider()

    else:

        st.write("No conversation yet.")
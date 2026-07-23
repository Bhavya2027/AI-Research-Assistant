import os
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader


def load_pdfs(folder_path):
    documents = []

    st.write("📂 Entered load_pdfs()")

    if not os.path.exists(folder_path):
        st.error(f"Folder not found: {folder_path}")
        return []

    pdf_files = [
        f for f in os.listdir(folder_path)
        if f.lower().endswith(".pdf")
    ]

    st.write("PDF Files Found:", pdf_files)

    for pdf in pdf_files:

        pdf_path = os.path.join(folder_path, pdf)

        st.write(f"Loading: {pdf}")

        try:
            loader = PyPDFLoader(pdf_path)

            docs = loader.load()

            st.write(f"{pdf} -> {len(docs)} pages")

            for doc in docs:
                doc.metadata["source_pdf"] = pdf

            documents.extend(docs)

        except Exception as e:
            st.error(f"Error loading {pdf}")
            st.exception(e)

    st.write("Total Documents:", len(documents))

    return documents

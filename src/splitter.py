from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    """
    Split documents into smaller chunks while preserving metadata.
    """

    if not documents:
        raise ValueError("No documents provided for splitting.")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )

    chunks = text_splitter.split_documents(documents)

    print(f"Original Documents : {len(documents)}")
    print(f"Total Chunks Created: {len(chunks)}")

    # Show metadata of first few chunks (for verification)
    print("\nSample Metadata:")
    for i, chunk in enumerate(chunks[:3]):
        print(f"Chunk {i + 1}: {chunk.metadata}")

    return chunks
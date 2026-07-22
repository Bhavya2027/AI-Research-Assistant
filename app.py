from src.loader import load_pdf
from src.splitter import split_documents
from src.embeddings import get_embedding_model
from src.vectordb import create_vector_db
from src.retriever import load_vector_db, get_retriever
from src.llm import get_llm
from src.rag import generate_answer

pdf_path = "data/pdfs/AI.pdf"

# Step 1: Read PDF
documents = load_pdf(pdf_path)

# Step 2: Split into chunks
chunks = split_documents(documents)

# Step 3: Load embedding model
embedding_model = get_embedding_model()

# Step 4: Create vector database
create_vector_db(chunks, embedding_model)

# Step 5: Load vector database
vector_db = load_vector_db(embedding_model)

# Step 6: Create retriever
retriever = get_retriever(vector_db)

# Step 7: Load LLM
llm = get_llm()

# Step 8: Ask a question
question = "What are embeddings?"

# Step 9: Retrieve relevant chunks
retrieved_docs = retriever.invoke(question)

# Step 10: Generate answer
answer = generate_answer(question, retrieved_docs, llm)

print("\nQuestion:\n")
print(question)

print("\nAnswer:\n")
print(answer)
# AI Research Assistant

An intelligent AI-powered Research Assistant that answers user questions by retrieving information from PDF documents and the web using **Retrieval-Augmented Generation (RAG)**.

The application combines local document retrieval with online search to generate accurate, context-aware responses while displaying the sources used to create the answer.

Built with **Python**, **LangChain**, **Google Gemini**, **ChromaDB**, and **Streamlit**, this project demonstrates modern AI application development using Large Language Models (LLMs) and Retrieval-Augmented Generation.

# Overview

The AI Research Assistant allows users to ask natural language questions related to research topics.

The assistant first searches uploaded PDF documents using semantic search. If sufficient information is unavailable, it automatically searches the web and combines both sources to generate a comprehensive answer.

The application maintains conversation history, displays source references, and provides a clean Streamlit interface for an interactive user experience.


# Features

-  Answer questions from PDF documents
-  Search the web when PDF information is insufficient
-  Retrieval-Augmented Generation (RAG)
-  Google Gemini LLM integration
-  Semantic document search using embeddings
-  Conversation history
-  Source citations for transparency
-  Fast vector search using ChromaDB
-  Modern Streamlit Web Interface
-  Professional error handling
-  Support for multiple PDF documents
-  Automatic fallback from PDF search to web search



# How It Works

1. Upload one or more PDF documents.
2. Documents are loaded and split into smaller chunks.
3. Each chunk is converted into vector embeddings.
4. Embeddings are stored in ChromaDB.
5. User asks a question.
6. Relevant document chunks are retrieved.
7. If document information is insufficient, the assistant searches the web.
8. Gemini generates a final summarized response using both PDF and web context.
9. The assistant displays the answer along with source references.

# Architecture

```
                User Question
                      │
                      ▼
          Retrieve Relevant PDF Chunks
                      │
          ┌───────────┴────────────┐
          │                        │
     Relevant Found?            Not Enough Data
          │                        │
          ▼                        ▼
     PDF Context             DuckDuckGo Search
          │                        │
          └───────────┬────────────┘
                      ▼
               Google Gemini LLM
                      ▼
             Final Summarized Answer
                      ▼
           Answer + Source Citations
```

# Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core Programming Language |
| LangChain | RAG Pipeline |
| Google Gemini | Large Language Model |
| ChromaDB | Vector Database |
| Sentence Transformers | Text Embeddings |
| DuckDuckGo Search | Web Search |
| Streamlit | Web Interface |
| PyPDF | PDF Loading |
| FAISS / Chroma | Semantic Retrieval |
| dotenv | Environment Variables |

# Project Structure

```
AI-Research-Assistant/
│
├── data/
│   └── pdfs/
│       └── sample.pdf
│
├── chroma_db/
│
├── src/
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── llm.py
│   ├── web_search.py
│   ├── rag.py
│   └── utils.py
│
├── app.py
├── streamlit_app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

# Installation


## Navigate into the Project

```bash
cd AI-Research-Assistant
```

## Create a Virtual Environment

```bash
python -m venv venv
```

## Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## 6. Configure Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

# Running the Application

## Terminal Version

```bash
python app.py
```

## Streamlit Version

```bash
streamlit run streamlit_app.py
```

# Example Questions

- What is Retrieval-Augmented Generation?
- Summarize this research paper.
- Explain the conclusion section.
- What are the advantages of Transformer models?
- Compare CNN and Vision Transformers.
- What does the uploaded PDF say about reinforcement learning?


# Streamlit Interface

The Streamlit application provides:

- Upload PDF documents
- Ask research questions
- View generated responses
- Display retrieved document context
- Show web search results
- Conversation history
- Source citations
- Professional error messages

# Key Concepts Used

- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- Semantic Search
- Vector Embeddings
- Vector Databases
- Prompt Engineering
- Information Retrieval
- Natural Language Processing
- Context-Aware AI
- Document Question Answering

# Error Handling

The application gracefully handles:

- Missing PDF files
- Invalid API keys
- Empty user questions
- No internet connection
- Empty search results
- Missing embeddings
- Vector database errors
- Unsupported file formats

# Future Improvements

- PDF Upload from UI
- Multiple LLM Support (OpenAI, Claude, Llama)
- Research Report Generation
- Export Answers to PDF
- Voice Input
- Multi-language Support
- OCR for Scanned PDFs
- Citation Formatting (APA, MLA, IEEE)
- User Authentication
- Cloud Deployment


# Learning Outcomes

This project demonstrates practical experience with:

- Building RAG Applications
- LangChain Workflows
- Vector Databases
- Embedding Models
- Google Gemini API
- Semantic Search
- Prompt Engineering
- Streamlit Development
- AI-Powered Search Systems
- End-to-End LLM Applications

---

#  Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to your branch

```bash
git push origin feature-name
```

5. Open a Pull Request


# Author

**Bhavya Bhardwaj**

Electronics & Communication Engineering Student

Passionate about Artificial Intelligence, Machine Learning, and Software Development.


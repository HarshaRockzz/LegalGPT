# LegalGPT: LLM-based Legal ChatBot

LegalGPT is a Large Language Model (LLM) based chatbot designed to provide legal information. The chatbot utilizes RAG architecture, advanced language models, and embeddings to retrieve and generate contextually relevant answers from a provided legal document corpus. This project specifically focuses on the Indian Penal Code and other related legal documents.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Architecture](#architecture)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Challenges Faced](#challenges-faced)
- [Future Improvements](#future-improvements)
- [Detailed System Architecture](#detailed-system-architecture)
- [Deployed Website](#deployed-website)

## Introduction

LegalGPT aims to assist users by providing accurate and concise legal information based on the Indian Penal Code and related legal documents. The chatbot retrieves relevant context from the knowledge base to answer user queries efficiently.

## Features

- Conversational interface for querying legal information
- Uses FAISS for efficient vector search
- Embeds documents using Google Generative AI Embeddings
- Handles large document sets by splitting and batching
- Provides sources for retrieved information

## Architecture

The architecture of LegalGPT includes the following components:

1. **Document Loader**: Loads legal documents from a directory of PDF files.
2. **Text Splitter**: Splits documents into manageable chunks for embedding.
3. **Embeddings**: Uses Google Generative AI Embeddings to transform text into vector representations.
4. **Vector Store**: Utilizes FAISS to store and retrieve document embeddings.
5. **LLM**: Uses the ChatGroq API to generate responses based on retrieved documents and user queries.
6. **Memory**: Maintains a conversation buffer to provide context in conversations.

## Setup and Installation

### Prerequisites

- Python 3.10
- Streamlit
- LangChain Community
- Google Generative AI
- FAISS

### Installation Steps

1. **Clone the Repository**

```bash
   git clone https://github.com/HarshaRockzz/LegalGPT.git
   cd LegalGPT
```

2.  **Set Up and Activate Virtual Environment**

```bash
    conda create -p venv python==3.10
    conda activate C:\directory\venv
```

3. **Install Dependencies**

```bash
    pip install -r requirements.txt
```

4. **Set Up Environment Variables**

Create a .env file in the project root directory and add your API keys:
```bash
    GOOGLE_API_KEY=your_google_api_key
    GROQ_API_KEY=your_groq_api_key
```

5. **Split, Embed, and Save Documents**

Run the following script to load, split, embed, and save your legal documents:
```bash
    python ingestion.py
```

## Usage

Run the Streamlit Application

```bash
streamlit run app.py
```

## Challenges Faced

1. **Handling Large Documents**: Splitting and embedding large legal documents while maintaining context was a challenge.
2. **Latency Issues**: Query processing time increased with a large dataset, requiring optimization in FAISS indexing.
3. **API Rate Limits**: Google Generative AI API rate limits affected batch processing efficiency.
4. **Context Relevance**: Ensuring the chatbot retrieved the most relevant legal information was complex.
5. **Scalability**: Managing and updating a growing legal document corpus required better indexing strategies.

## Future Improvements

1. **Improved Query Handling**: Implementing a hybrid retrieval mechanism combining keyword and vector search.
2. **Multi-Language Support**: Expanding support to regional Indian languages for accessibility.
3. **Better Context Awareness**: Enhancing memory to maintain long conversations more effectively.
4. **Optimization of FAISS Indexing**: Reducing search time with optimized indexing techniques.
5. **Deployment on Multiple Platforms**: Expanding beyond Streamlit to web apps and mobile applications.
6. **Legal Case Precedents**: Integrating case law to provide references for legal queries.

## Detailed System Architecture

### Flow of Query Processing

1. **User Query**: The user submits a legal question via the chatbot interface.
2. **Document Retrieval**: FAISS searches the vector database for relevant legal text chunks.
3. **Query & Summarization Agents**:
   - The **retriever agent** fetches relevant documents.
   - The **summarization agent** condenses long responses for clarity.
4. **LLM Processing**:
   - The ChatGroq API processes the user query along with the retrieved text.
   - Generates an accurate and context-aware legal response.
5. **Response Delivery**: The chatbot presents the response along with references.

### Role of FAISS, Embeddings, and LLMs

- **FAISS**: Efficiently indexes and retrieves vectorized document embeddings for quick search.
- **Embeddings**: Transforms text into numerical vectors using Google Generative AI to enable semantic search.
- **LLM (ChatGroq API)**: Processes retrieved documents and user queries to generate legal answers.

## Deployed Website

LegalGPT is also deployed on Streamlit Cloud. You can access the chatbot directly via the following link:

[LegalGPT](https://harsha-legalgpt.streamlit.app/)


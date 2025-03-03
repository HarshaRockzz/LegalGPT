LegalGPT: LLM-based Legal ChatBot

 

LegalGPT is a Large Language Model (LLM) based chatbot designed to provide legal information. The chatbot utilizes RAG architecture, advanced language models, and embeddings to retrieve and generate contextually relevant answers from a provided legal document corpus. This project specifically focuses on the Indian Penal Code and other related legal documents.

Table of Contents

Introduction

Features

Architecture

Setup and Installation

Usage

Deployed Website

Future Enhancements

Introduction

LegalGPT aims to assist users by providing accurate and concise legal information based on the Indian Penal Code and related legal documents. The chatbot retrieves relevant context from the knowledge base to answer user queries efficiently.

Features

Conversational interface for querying legal information

Uses FAISS for efficient vector search

Embeds documents using Google Generative AI Embeddings

Handles large document sets by splitting and batching

Provides sources for retrieved information

Deployed online for easy access

Memory buffer to maintain conversation history

Architecture

The architecture of LegalGPT includes the following components:

Document Loader: Loads legal documents from a directory of PDF files.

Text Splitter: Splits documents into manageable chunks for embedding.

Embeddings: Uses Google Generative AI Embeddings to transform text into vector representations.

Vector Store: Utilizes FAISS to store and retrieve document embeddings.

LLM: Uses the ChatGroq API to generate responses based on retrieved documents and user queries.

Memory: Maintains a conversation buffer to provide context in conversations.

Web Interface: Built using Streamlit for user-friendly interaction.

Setup and Installation

Prerequisites

Python 3.10

Streamlit

LangChain Community

Google Generative AI

FAISS

Installation Steps

Clone the Repository

   git clone https://github.com/yourusername/lawgpt.git
   cd legalgpt

Set Up and Activate Virtual Environment

    conda create -p venv python==3.10
    conda activate C:\directory\venv

Install Dependencies

    pip install -r requirements.txt

Set Up Environment Variables

Create a .env file in the project root directory and add your API keys:

    GOOGLE_API_KEY=your_google_api_key
    GROQ_API_KEY=your_groq_api_key

Split, Embed and Save Documents

Run the following script to load, split, embed, and save your legal documents:

    python ingestion.py

Usage

Run the Streamlit Application:

streamlit run app.py

Deployed Website

LegalGPT is also deployed on Streamlit Cloud. You can access the chatbot directly via the following link:

🔗 LegalGPT Chatbot

Future Enhancements

Multilingual Support: Add support for regional languages for better accessibility.

Enhanced UI/UX: Improve the chatbot interface for better usability.

More Legal Domains: Expand beyond the Indian Penal Code to include civil, corporate, and tax law.

User Authentication: Implement authentication for personalized responses.

Chat History & Export: Allow users to save and download chat history.

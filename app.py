import streamlit as st
import os
import time
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationalRetrievalChain
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ['GOOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

# Streamlit UI setup
st.set_page_config(page_title="LegalGPT - AI Legal Advisor", page_icon="⚖️", layout="wide")

# Custom CSS Styling
st.markdown(
    """
    <style>
        body {
            background-color: #f8f9fa;
        }
        .main-title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #2c3e50;
            padding: 10px 0;
        }
        .chat-container {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .user-message {
            background-color: #3498db;
            color: white;
            padding: 10px;
            border-radius: 10px;
            margin: 10px 0;
        }
        .bot-message {
            background-color: #2ecc71;
            color: white;
            padding: 10px;
            border-radius: 10px;
            margin: 10px 0;
        }
        .reset-button button {
            background-color: #e74c3c !important;
            color: white !important;
            font-size: 16px;
            border-radius: 5px;
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Reset conversation function
def reset_conversation():
    st.session_state.messages = []
    st.session_state.memory.clear()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferWindowMemory(k=2, memory_key="chat_history", return_messages=True)

# Initialize embeddings and vector store
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
db = FAISS.load_local("my_vector_store", embeddings, allow_dangerous_deserialization=True)
db_retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 4})

# Define the prompt template
prompt_template = """
<s>[INST]You are a legal assistant providing professional legal advice based on the Indian Penal Code. Keep responses factual and relevant.
CONTEXT: {context}
CHAT HISTORY: {chat_history}
QUESTION: {question}
ANSWER:
</s>[INST]
"""
prompt = PromptTemplate(template=prompt_template, input_variables=['context', 'question', 'chat_history'])

# Initialize the LLM
llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama3-70b-8192")

# Set up the QA chain
qa = ConversationalRetrievalChain.from_llm(
    llm=llm,
    memory=st.session_state.memory,
    retriever=db_retriever,
    combine_docs_chain_kwargs={'prompt': prompt}
)

# UI Layout
st.markdown('<div class="main-title">⚖️ Legal ChatBot - AI Legal Advisor</div>', unsafe_allow_html=True)

chat_container = st.container()

# Display previous messages
with chat_container:
    for message in st.session_state.messages:
        role = message.get("role")
        content = message.get("content")
        css_class = "user-message" if role == "user" else "bot-message"
        st.markdown(f'<div class="{css_class}">{content}</div>', unsafe_allow_html=True)

# User input
input_prompt = st.chat_input("Ask me about Indian law...")

if input_prompt:
    with chat_container:
        st.markdown(f'<div class="user-message">{input_prompt}</div>', unsafe_allow_html=True)
    
    st.session_state.messages.append({"role": "user", "content": input_prompt})
    
    with chat_container:
        with st.spinner("Analyzing legal context... ⏳"):
            result = qa.invoke(input=input_prompt)
            full_response = result["answer"]
            time.sleep(0.5)
            
        st.markdown(f'<div class="bot-message">{full_response}</div>', unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
    
    st.button('🔄 Reset Chat', on_click=reset_conversation, key="reset", help="Clear conversation history", use_container_width=True)


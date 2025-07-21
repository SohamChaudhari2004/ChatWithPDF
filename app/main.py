import streamlit as st
import PyPDF2
import os
from dotenv import load_dotenv
import chromadb
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter
from langchain_mistralai import ChatMistralAI
load_dotenv()

# Initialize ChromaDB client
chroma_client = chromadb.PersistentClient(path="chroma_db")

# Initialize LangChain MistralKAI LLM
mistral_llm = ChatMistralAI(
    api_key=os.getenv("MISTRAL_API_KEY"), model_name="mistral-large-latest")

@st.cache_data
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def create_rag_chain(text):
    # Split text into chunks
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = splitter.create_documents([text])

    # Create embeddings
    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")

    # Create Chroma vector store
    vectorstore = Chroma.from_documents(docs, embeddings, client=chroma_client, collection_name="pdf_rag")

    # Create RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=mistral_llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(),
        return_source_documents=True
    )
    return qa_chain

# Main Streamlit UI
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf", "docx"])

if uploaded_file is not None:
    text_content = extract_text_from_pdf(uploaded_file)
    st.success("PDF uploaded and text extracted successfully!")

    # Create RAG chain for the uploaded PDF
    qa_chain = create_rag_chain(text_content)

    user_question = st.text_input("Ask a question about the PDF content:")

    if user_question:
        try:
            result = qa_chain({"query": user_question})
            answer = result["result"]
            st.markdown(f"**Answer:**\n\n{answer}", unsafe_allow_html=True)
            # Optionally show source docs
            if "source_documents" in result:
                with st.expander("Source Documents"):
                    for i, doc in enumerate(result["source_documents"]):
                        st.markdown(f"**Chunk {i+1}:**\n{doc.page_content}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    st.write("Welcome to the PDF Chatbot application! (RAG with ChromaDB & MistralAI)")

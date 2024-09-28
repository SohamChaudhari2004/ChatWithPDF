import streamlit as st
import PyPDF2
import os
from dotenv import load_dotenv
import groq

# Load environment variables
load_dotenv()

# Initialize Groq client
client = groq.Client(api_key=os.getenv("GROQ_API_KEY"))

#cache extracted text for querying
@st.cache_data
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


#pass the prompt to the groq API.
def get_groq_response(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="mixtral-8x7b-32768",
        max_tokens=1024,
    )
    return chat_completion.choices[0].message.content

st.title("PDF Chatbot")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    text_content = extract_text_from_pdf(uploaded_file)
    st.success("PDF uploaded and text extracted successfully!")

    user_question = st.text_input("Ask a question about the PDF content:")
    
    if user_question:
        prompt = f"Based on the following text from a PDF:\n\n{text_content}\n\nQuestion: {user_question}\n\nAnswer:"
        
        try:
            response = get_groq_response(prompt)
            st.code(f"**Answer:**\n\n{response}" , language='markdown', wrap_lines=True)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    st.write("Welcome to the PDF Chatbot application!")
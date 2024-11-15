## https://chatwithpdf-sohamchaudhari2004.streamlit.app/
PDF Chatbot Application
This is a simple PDF Chatbot application built using Streamlit, PyPDF2, and the Groq API. The application allows users to upload a PDF file, extract its text, and interact with it by asking questions based on the content of the PDF.

Features:
Upload a PDF file and extract text content from it.
Ask questions about the PDF content.
Get responses from a Groq AI model (mixtral-8x7b-32768) based on the extracted text.
Requirements:
Python 3.x
Streamlit
PyPDF2
Groq API client
python-dotenv
Installation:
Step 1: Install Dependencies
To get started, clone this repository and navigate to the project directory. Then, install the required dependencies:

bash
Copy code
pip install streamlit pypdf2 groq python-dotenv
Step 2: Set up Environment Variables
Create a .env file in the root directory of the project.
Add your Groq API key in the .env file:
bash
Copy code
GROQ_API_KEY=your_groq_api_key
Step 3: Running the Application
After installing the dependencies and setting up the .env file, you can run the application using Streamlit:

bash
Copy code
streamlit run app/main.py
Step 4: Interacting with the Application
Upload a PDF file using the file uploader.
After the file is uploaded, the content of the PDF is extracted.
Type your question in the input field, and the app will use the Groq model to provide an answer based on the content of the PDF.
Application Flow:
PDF Upload: The app allows users to upload a PDF file from their local device.
Text Extraction: The PyPDF2 library extracts text content from the uploaded PDF file.
Question & Answer: Users can ask questions related to the content, and the Groq model provides answers based on the extracted text.
Example Use Case:
Upload a research paper PDF.
Ask a question like, "What is the conclusion of the paper?"
The model will generate a response based on the paper's content.
Troubleshooting:
Error in uploading PDF: Ensure the PDF is not corrupted and is in a supported format.
Model response issue: Check if your Groq API key is set correctly in the .env file.

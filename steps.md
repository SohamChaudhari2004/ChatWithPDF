Steps:

1. import libraries used for the application
```
pip install streamlit pypdf2 groq python-dotenv
```
2. Create a Streamlit user-interface to accept pdf files from the local device using the file_uploader method of streamlit library.
```
st.file_uploader("Choose a PDF file", type="pdf")
```
3. Write a function to extract text from the pdf using the PyPDF2 library's PdfReader method
```
PyPDF2.PdfReader(pdf_file)
```
4. Create a function to pass the prompt to the Groq API that uses the 'mixtral-8x7b-32768' model and generates the response based on the prompt.
```
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
```

5. Construct the application arranging all these steps above.

6. Run the python application on Streamlit
```
streamlit run app/main.py
```


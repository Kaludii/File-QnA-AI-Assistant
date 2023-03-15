import openai
import pandas as pd
import streamlit as st
import io
from PyPDF2 import PdfReader
from PIL import Image

st.title("File Q&A AI Assistant")
st.write("This app allows you to upload a CSV or PDF file, or enter text and ask questions related to the content. The app uses OpenAI's ChatGPT model to assist you in answering your questions about the uploaded content, which is streamed back in real time similar to the ChatGPT interface.")

messages = [
    {"role": "system", "content": "You are a professional Question and Answer AI Assistant helping with information in regards to a csv, pdf, and text input file."},
]

def chatbot(api_key, query_text, file_data):
    openai.api_key = api_key
    if query_text:
        messages.append({"role": "user", "content": query_text})
    if file_data:
        messages.append({"role": "user", "content": f"{file_type} File Type: {file_data}"})
    
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages, stream=True
    )
    
    response_text = st.empty()
    response_line = ""
    
    for chunk in chat:
        chunk_message = chunk['choices'][0]['delta']
        if chunk_message.get('content'):
            response_line += chunk_message['content']
            response_text.write("Response: " + response_line)
    
    messages.append({"role": "assistant", "content": response_line})

api_key = st.text_input("OpenAI API Key", type="password", key=2)
query_text = st.text_area("Question", key="input", height=100)
file_type = st.selectbox("Select File Type", options=["CSV", "PDF", "Text"])

file_data = None

if file_type == "CSV":
    file = st.file_uploader("Upload CSV file", type="csv")
    if file:
        df = pd.read_csv(file)
        st.write("Uploaded CSV file:")
        st.write(df)       
        file_data = df.to_csv(index=False)
elif file_type == "PDF":
    file = st.file_uploader("Upload PDF file", type="pdf")
    if file:
        pdf_reader = PdfReader(file)
        file_data = ""
        for page in pdf_reader.pages:
            file_data += page.extract_text()
        st.write("Uploaded PDF file:")
        st.write(file_data)
else:
    file_data = st.text_area("Enter text here")

if st.button("Send"):
    try:
        chatbot(api_key, query_text, file_data)
    except Exception as e:
        st.error(str(e))

st.markdown("")
st.markdown("---")
st.markdown("")
st.markdown("<p style='text-align: center'><a href='https://github.com/Kaludii'>Github</a> | <a href='https://huggingface.co/Kaludi'>HuggingFace</a></p>", unsafe_allow_html=True)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

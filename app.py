import openai
import pandas as pd
import streamlit as st
import io
from PyPDF2 import PdfReader
from PIL import Image

# Add a title and description
st.title("File Q&A AI Assistant")
st.write("This app allows you to upload a CSV or PDF file, or enter text and ask questions related to the content. The app uses OpenAI's ChatGPT model to assist you in answering your questions about the uploaded content.")

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
        model="gpt-3.5-turbo", messages=messages
    )
    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    if "InvalidRequestError" in reply:
        raise Exception(reply)
    return reply

api_key = st.text_input("OpenAI API Key", type="password", key=2)
query_text = st.text_area("Question", key="input", height=150)
file_type = st.selectbox("Select File Type", options=["CSV", "PDF", "Text"])

# Initialize file_data variable with a default value of None
file_data = None

if file_type == "CSV":
    file = st.file_uploader("Upload CSV file", type="csv")
    if file:
        # read the csv file into a pandas dataframe
        df = pd.read_csv(file)
        st.write("Uploaded CSV file:")
        # display the dataframe as a table
        st.write(df)       
        # update file_data with csv data
        file_data = df.to_csv(index=False)
elif file_type == "PDF":
    file = st.file_uploader("Upload PDF file", type="pdf")
    if file:
        # Initialize a PyPDF2 PdfReader object
        pdf_reader = PdfReader(file)

        # Extract the text from the PDF file
        file_data = ""
        for page in pdf_reader.pages:
            file_data += page.extract_text()

        # Display the uploaded PDF file
        st.write("Uploaded PDF file:")
        st.write(file_data)

else:
    file_data = st.text_area("Enter text here")

output_text = st.empty()

if st.button("Send"):
    try:
        response = chatbot(api_key, query_text, file_data)
        st.write("Response:")
        st.write(response)
    except Exception as e:
        st.error(str(e))

st.markdown("")
st.markdown("---")
st.markdown("")
st.markdown("<p style='text-align: center'><a href='https://github.com/Kaludii'>Github</a> | <a href='https://huggingface.co/Kaludi'>HuggingFace</a></p>", unsafe_allow_html=True)

import openai
import pandas as pd
import streamlit as st
import io
from PyPDF2 import PdfReader
from PIL import Image
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import matplotlib.pyplot as plt
import os

st.title("File Q&A AI Assistant with PandasAI")
st.write("This app allows you to upload a CSV or PDF file, or enter text and ask questions related to the content. The app uses PandasAI with OpenAI's API to assist you in answering your questions about the uploaded content, which is streamed back in real time similar to the ChatGPT interface.")

def chatbot(api_key, query_text, file_data):
    openai.api_key = api_key
    if query_text and file_data is not None:
        with st.spinner("Generating response..."):
            llm = OpenAI(api_token=api_key)
            pandas_ai = PandasAI(llm)
            x = pandas_ai.run(file_data, prompt=query_text)

            if plt.get_fignums():
                plt.savefig('temp_chart.png')
                plt.close()
                im = Image.open('temp_chart.png')
                st.image(im)
                os.remove('temp_chart.png')

            if x is not None:
                st.write(x)

api_key = st.text_input("OpenAI API Key", type="password", key=2)
query_text = st.text_area("Question", key="input", height=100)
file_type = st.selectbox("Select File Type (Current only CSV)", options=["CSV", "PDF", "Text"])

file_data = None

if file_type == "CSV":
    file = st.file_uploader("Upload CSV file", type="csv")
    if file:
        df = pd.read_csv(file)
        st.write("Uploaded CSV file:")
        st.write(df)       
        file_data = df
elif file_type == "PDF":
    file = st.file_uploader("Upload PDF file", type="pdf")
    if file:
        pdf_reader = PdfReader(file)
        file_data = ""
        for page in pdf_reader.pages:
            file_data += page.extract_text()

        st.write("Uploaded PDF file:")
        with st.container():
            st.markdown(
                "<style>"
                ".scrollable {"
                "    max-height: 300px;"
                "    overflow-y: auto;"
                "}"
                "</style>"
                '<div class="scrollable">'
                + file_data.replace("\n", "<br>")
                + "</div>",
                unsafe_allow_html=True,
            )
            st.markdown("")
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
import openai
import pandas as pd
import streamlit as st
from PyPDF2 import PdfReader
from PIL import Image
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
from langchain.llms import OpenAI as LangChainOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
import os
import matplotlib.pyplot as plt

# Set streamlit page layout to wide mode
st.set_page_config(page_title="File Q&A AI Assistant 🤖" , page_icon="🤖")

# Removes streamlit hyperlink at the bottom of the page
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("File Q&A AI Assistant 🤖")
st.write("This interface allows users to upload a CSV, PDF, or enter text and ask questions related to the content.")

with st.expander("Expand to see how it works."):
    st.markdown("""
    - **CSV Files**: Upload your CSV file and interact directly with the data. You can ask specific questions to get insights or request visualizations to generate a graph directly from the CSV data.
    - **PDF Files**: Upload a PDF file annd ask questions related to it. The interface will to analyze the text and provide answers.
    - **Text Input**: Enter any text and ask questions related to it. The interface will analyze the content and provide answers.
    """)

def chatbot(api_key, query_text, file_data, file_type):
    openai.api_key = api_key
    if query_text and file_data is not None:
        with st.spinner("Generating response..."):
            try:
                if file_type == "CSV":
                    llm = OpenAI(api_token=api_key)
                    pandas_ai = PandasAI(llm)

                    # Make sure file_data is a DataFrame for CSV
                    if not isinstance(file_data, pd.DataFrame):
                        df = pd.read_csv(file_data)
                    else:
                        df = file_data

                    x = pandas_ai.run(df, prompt=query_text)

                    if plt.get_fignums():
                        plt.savefig('temp_chart.png')
                        plt.close()
                        im = Image.open('temp_chart.png')
                        st.image(im)
                        os.remove('temp_chart.png')

                    if x is not None:
                        st.write(x)

                else:
                    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len)
                    chunks = text_splitter.split_text(file_data)

                    embeddings = OpenAIEmbeddings(api_key=api_key)
                    knowledge_base = FAISS.from_texts(chunks, embeddings)

                    llm = LangChainOpenAI(api_key=api_key)
                    chain = load_qa_chain(llm, chain_type="map_rerank")
                    
                    docs = knowledge_base.similarity_search(query_text, top_k=5)
                    response = chain.run(input_documents=docs, question=query_text)

                    if response is not None:
                        st.write(response)
            except Exception as e:
                st.error(f"An error occurred: {e}")



api_key = st.text_input("OpenAI API Key", type="password")
query_text = st.text_area("Question", height=100)
file_type = st.selectbox("Select File Type", options=["CSV", "PDF", "Text"])

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
        file_data = "".join(page.extract_text() for page in pdf_reader.pages)

        st.write("Uploaded PDF file:")
        st.text_area("PDF content", value=file_data, height=300, disabled=True)
else:
    file_data = st.text_area("Enter text here")

if st.button("Send"):
    try:
        chatbot(api_key, query_text, file_data, file_type)
    except Exception as e:
        st.error(str(e))

st.markdown("---")
st.markdown("<p style='text-align: center'><a href='https://github.com/Kaludii'>Github</a> | <a href='https://huggingface.co/Kaludi'>HuggingFace</a></p>", unsafe_allow_html=True)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

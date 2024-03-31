# File Q&A AI Assistant 🤖

This is a Streamlit app that allows users to upload CSV, PDF files, or enter text and ask questions related to the content. The app uses OpenAI's API along with PandasAI for CSV files and LangChain for PDF and text files to provide quick answers in real-time.

## Web App
Click [Here](https://huggingface.co/spaces/Kaludi/File-QnA-AI-Assistant_App "Here") to view this app online!

![image](https://github.com/Kaludii/File-QnA-AI-Assistant/assets/63890666/fb7b2962-1410-4d06-b563-0428f8369d1d)
![image](https://github.com/Kaludii/File-QnA-AI-Assistant/assets/63890666/c304d98d-87aa-4c9e-8373-a6ea34589b40)


## Features

- Users can upload CSV, PDF files, or enter text to ask questions related to the content.
- PandasAI is used for CSV uploads, along with asking questions, users can also request visualizations to generate a graph directly from the CSV data.
- For PDF and text inputs, LangChain is used to answer questions related to the content, no matter how long it is.

## Usage

### CSV File

- Upload a CSV file to interact with the data through questions or request visualizations directly.

### PDF File and Text

- Upload a PDF file or enter text to get answers to your questions based on the content.

### Asking Questions

- Enter your question in the "Question" field and click "Send" to receive answers based on the uploaded content or entered text.

## Requirements

- Python 3.6 or higher
- Streamlit
- openai
- pandasai==0.2.2
- PyPDF2
- Pillow
- LangChain
- docarray
- matplotlib
- pypdf
- tiktoken
- faiss-cpu

## Installation

1.  Clone the repository:

`git clone https://github.com/Kaludii/File-QnA-AI-Assistant.git` 

2.  Install the required packages:
To run this app, type `pip install -r requirements.txt` to automatically download all necessary dependencies, including Streamlit, OpenAI, Pandas, PyPDF2, Pillow, and LangChain.

3.  Run the app:

`streamlit run app.py`

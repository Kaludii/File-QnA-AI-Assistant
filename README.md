
# File Q&A AI Assistant

This is a Streamlit app that allows users to upload CSV or PDF files, or enter text and ask questions related to the content. The app uses OpenAI's ChatGPT model to assist users in answering their questions about the uploaded content, which is streamed back in real time similar to the ChatGPT interface.

# Web App
Click [Here](https://huggingface.co/spaces/Kaludi/File-QnA-AI-Assistant_App "Here") To View This App Online!

![image](https://user-images.githubusercontent.com/63890666/224580639-2aeec181-e7ad-446a-af69-0d2bfea33dff.png)


## Features

-   Users can upload CSV or PDF files, or enter text and ask questions related to the content.
-   The app uses OpenAI's ChatGPT model to generate responses to user questions.
-   Users can see the uploaded file as a table or text.
-   The app can handle large PDF files by processing one page at a time.
-   Users can easily run the app locally with minimal setup using Streamlit.


## Usage

When you run the app, you will see a title and description explaining what the app does. You will also see input fields for the OpenAI API key, question, and file type. You can enter your OpenAI API key and question, and select the file type you want to upload.

### CSV File

If you select "CSV" as the file type, you will be prompted to upload a CSV file. Once you upload the file, it will be displayed as a table, and the file data will be stored as a CSV string.

### PDF File

If you select "PDF" as the file type, you will be prompted to upload a PDF file. Once you upload the file, it will be displayed as text, and the file data will be stored as a string.

### Text

If you select "Text" as the file type, you will be prompted to enter text. The text you enter will be stored as a string.

### Asking Questions

Once you have uploaded a file or entered text, you can ask questions related to the content. Type your question in the "Question" field and click the "Send" button. The app will use OpenAI's ChatGPT model to generate a response to your question and display it below the "Send" button.

## Requirements

-   Python 3.6 or higher
-   Streamlit
-   openai
-   pandas
-   PyPDF2
-   Pillow

## Installation

1.  Clone the repository:

`git clone https://github.com/Kaludii/File-QnA-AI-Assistant.git` 

2.  Install the required packages:
To run this app, you will need to install the following dependencies or type `pip install -r requirements.txt` to automatically download:

-   `streamlit`
-   `openai`
-   `pandas`
-   `PyPDF2`
-   `Pillow`

You can install them using pip:
`pip install openai pandas streamlit PyPDF2 Pillow` 

3.  Run the app:

`streamlit run app.py`

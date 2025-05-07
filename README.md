# text_summarizer_AI_Agent

This is a Streamlit application that uses AI to summarize articles from any URL. It uses the BART-large-CNN model from Hugging Face for summarization and newspaper3k for article extraction.

## Features

- Extract and summarize articles from any URL
- View original article text
- Download summaries
- Clean and modern UI
- Handles long articles by chunking

## Setup

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to the URL shown in the terminal (usually http://localhost:8501)
3. Paste an article URL in the input field
4. Wait for the summary to be generated
5. View and download the summary

## Requirements

- Python 3.7+
- See requirements.txt for package dependencies

## Note

The first time you run the app, it will download the BART-large-CNN model, which might take a few minutes depending on your internet connection. 
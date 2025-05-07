import streamlit as st
import requests
from newspaper import Article
from transformers import pipeline
import torch
import os

# Set page config
st.set_page_config(
    page_title="Article Summarizer",
    page_icon="📝",
    layout="centered"
)

# Initialize the summarization pipeline
@st.cache_resource
def load_summarizer():
    try:
        # Force PyTorch device
        device = 0 if torch.cuda.is_available() else -1
        return pipeline(
            "summarization",
            model="facebook/bart-large-cnn",
            device=device,
            framework="pt"  # Explicitly use PyTorch
        )
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

def extract_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        st.error(f"Error extracting article: {str(e)}")
        return None

def summarize_text(text, max_length=130, min_length=30):
    if not text:
        return None
    
    try:
        # Split text into chunks if it's too long
        max_chunk_length = 1024
        chunks = [text[i:i + max_chunk_length] for i in range(0, len(text), max_chunk_length)]
        
        summarizer = load_summarizer()
        if summarizer is None:
            return None
            
        summaries = []
        
        for chunk in chunks:
            summary = summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)
            summaries.append(summary[0]['summary_text'])
        
        return " ".join(summaries)
    except Exception as e:
        st.error(f"Error during summarization: {str(e)}")
        return None

# App title and description
st.title("📝 Article Summarizer")
st.markdown("""
This app uses AI to summarize articles from any URL. Simply paste the article URL below and get a concise summary!
""")

# URL input
url = st.text_input("Enter the article URL:", placeholder="https://example.com/article")

if url:
    with st.spinner("Processing article..."):
        # Extract article text
        article_text = extract_article(url)
        
        if article_text:
            # Display original text
            with st.expander("View Original Article"):
                st.write(article_text)
            
            # Generate and display summary
            summary = summarize_text(article_text)
            if summary:
                st.subheader("Summary")
                st.write(summary)
                
                # Add download button for summary
                st.download_button(
                    label="Download Summary",
                    data=summary,
                    file_name="article_summary.txt",
                    mime="text/plain"
                ) 
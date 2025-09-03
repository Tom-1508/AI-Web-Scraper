import streamlit as st
from scrape import (
    scrape_website, 
    split_dom_content, 
    clean_body_content, 
    extract_body_content
)
from parse import parse_with_gemini   # ✅ updated import

# 🔒 Security Improvements --> Input Validation
from urllib.parse import urlparse
import re

def validate_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme in ("http", "https"), result.netloc])
    except:
        return False


st.title("AI Web Scrapper")
url = st.text_input("Enter a Website URL")

if st.button("Scrape Site"):
    if not validate_url(url):
        st.error("❌ Invalid URL. Please enter a valid website.")
        st.stop()

    st.write("Scraping the website...")
    try:
        result = scrape_website(url)
    except Exception as e:
        st.error(f"❌ Scraping failed: {str(e)}")
        st.stop()

    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    if not cleaned_content:
        st.warning("⚠️ No content found on this page.")
        st.stop()

    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)
    
    
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")
    
    if st.button("Parse Content"):
        if parse_description:
            st.write("⚡ Parsing the content... (faster with Gemini Flash)")

            dom_chunks = split_dom_content(st.session_state.dom_content) 
            with st.spinner("LLM working..."):
                result = parse_with_gemini(dom_chunks, parse_description)

            st.success("✅ Parsing complete")
            st.text_area("Parsed Result", result, height=300)

# Description: This is the main file that will be used to run the Streamlit app.
import streamlit as st
from scrape import scrape_website, extract_body_content, clean_body_content, split_dom_content
# HTML parsing
# BeautifulSoup is imported in scrape.py, so no need to import again here
from parse import parse_with_ollama

st.title("AI Web Scraper")

# Input for the website URL
url = st.text_input("Enter a Website URL")

if st.button("Scrape Website"):
    st.write("Scraping the website...")
    result = scrape_website(url)
    
    if result:
        # Extract, clean, and display the body content from the scraped website
        body_content = extract_body_content(result)
        cleaned_content = clean_body_content(body_content)
        
        # Store cleaned content in session state
        st.session_state['dom_content'] = cleaned_content
        
        # Display the cleaned DOM content within an expandable section
        with st.expander("View DOM Content"):
            st.text_area("DOM Content", cleaned_content, height=300)
    else:
        st.error("Failed to scrape the website.")

# If we have the DOM content stored in session state, enable parsing
if "dom_content" in st.session_state:
    # Text area for the user to input a description of what they want to parse
    parse_description = st.text_area("Describe what you want to parse")
    
    # Button to trigger the parsing process
    if st.button("Parse Content"):
        # Check if the user has entered a parse description
        if parse_description:
            st.write("Parsing content...")
            
            # Split the DOM content into manageable chunks
            dom_chunks = split_dom_content(st.session_state['dom_content'])
            
            # Parse the chunks using Ollama
            result = parse_with_ollama(dom_chunks, parse_description)
            
            # Display the parsed result
            st.write(result)
        else:
            st.error("Please provide a description for parsing.")

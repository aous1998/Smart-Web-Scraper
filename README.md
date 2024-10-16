# Smart-Web-Scraper
This project demonstrates how to build an AI-powered web scraper using Python. The application scrapes content from any website by leveraging the power of AI to extract and structure information based on user prompts. It uses several technologies, including:

Streamlit: To create a simple user interface for inputting website URLs and prompts.
Selenium: For web scraping, allowing us to automate browsing and extract content from websites.
LangChain: To interact with AI models that parse the website content and extract specific information based on user-defined prompts.
BeautifulSoup: For cleaning and processing the HTML content extracted from the website.
# Features:
Input any website URL and a prompt to extract specific data (e.g., e-commerce products, property listings, etc.).
Clean and filter HTML content to focus on relevant text data.
Split content into manageable chunks for AI processing to handle token limits.
Support for integration with AI models (e.g., GPT-4, LLaMA) via LangChain for intelligent data extraction.
# Technologies Used:
Python
Selenium: Automating web browsers to scrape websites.
BeautifulSoup: Parsing and cleaning HTML content.
LangChain: Interfacing with AI models to analyze and extract data.
Streamlit: A simple UI for input and output.
# How to run:
Install the required dependencies using pip install -r requirements.txt.
Set up a virtual environment.
Start the Streamlit app using streamlit run main.py.
Input a website URL and prompt to scrape and extract data.

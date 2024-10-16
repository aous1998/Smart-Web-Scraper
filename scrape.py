from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def scrape_website(website):
    print("Launching the Chrome browser")
    
    chrome_driver_path = "./chromedriver.exe"  # Ensure this path is correct for your setup
    
    # Set up Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode (no UI)
    options.add_argument("--disable-gpu")  # Disable GPU acceleration (optional)
    options.add_argument("--no-sandbox")  # Added for some environments
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    
    # Set up the Chrome driver service
    service = Service(chrome_driver_path)
    
    # Launch the Chrome browser
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get(website)
        
        # Wait for the body element to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        html = driver.page_source  # Get the page source
        
        return html
    
    except Exception as e:
        print(f"An error occurred while scraping the website: {e}")
        return None
    
    finally:
        driver.quit()  # Ensure the browser is closed even if an error occurs

def extract_body_content(html):
    soup = BeautifulSoup(html, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    
    # Remove script and style tags
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    
    # Get text from the body and clean it
    cleaned_content = soup.get_text(separator="\n")
    
    # Remove extra whitespace
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())
    
    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    # Split the content into batches of max_length characters
    return [dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)]

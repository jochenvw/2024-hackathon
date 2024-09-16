import json
import requests
import os
from bs4 import BeautifulSoup
from skills.summarize import summarize_text

def scrape_website(objective: str, url: str):
    """
    Scrapes the content of a website and optionally summarizes it.
    Args:
        objective (str): The objective or purpose for summarizing the text.
        url (str): The URL of the website to scrape.
    Returns:
        str: The scraped text or its summary if the text length exceeds 10000 characters.
    """

    headers = {
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/json',
    }

    data = {
        "url": url        
    }

    data_json = json.dumps(data)

    api_key = os.getenv("BROWSERLESS_API_KEY")
    response = requests.post(f"https://chrome.browserless.io/content?token={api_key}", headers=headers, data=data_json)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.get_text()
            
        if len(text) > 10000:
            output = summarize_text(objective,text)
            return output
        else:
            return text
    else:
        print(f"HTTP request failed with status code {response.status_code}")        

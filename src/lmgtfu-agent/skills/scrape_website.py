import json
import requests
import os
from bs4 import BeautifulSoup
from skills.summarize import summarize_text

def scrape_website(objective: str, url: str, summarizeText: bool = True) -> str:
    """
    Scrapes the content of a given website URL and optionally summarizes the text.
    Args:
        objective (str): The objective or purpose of scraping the website.
        url (str): The URL of the website to scrape.
        summarizeText (bool, optional): Flag to indicate whether to summarize the scraped text if it exceeds 10,000 characters. Defaults to True.
    Returns:
        str: The scraped (and optionally summarized) text content of the website.
    Raises:
        HTTPError: If the HTTP request to the scraping service fails.
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
    print(f"Scraping website {url}...")
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.get_text()

        if len(text) > 10000 or summarizeText:
            print(f"Scraped {len(text)} characters from the website. Summarizing the text...")
            output = summarize_text(objective,text)
            return output
        else:
            return text
    else:
        print(f"HTTP request failed with status code {response.status_code}")        

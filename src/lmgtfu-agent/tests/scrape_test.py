import unittest
import os
from dotenv import load_dotenv
from loguru import logger

# Import the skill to be tested
from skills.scrape_website import scrape_website

# Load environment variables from logfile
load_dotenv()

class test_site_scraping(unittest.TestCase):

    def test_learn_site_scraping(self):
        # Scrape the content of a website and summarize it - asserts that the result is not None
        result = scrape_website("summarize in 1 sentence", "https://learn.microsoft.com/en-us/azure/azure-functions/openapi-apim-integrate-visual-studio?tabs=isolated-process")

        print(result)

        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)
        self.assertLessEqual(len(result), 1000)

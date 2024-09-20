import unittest
import os
from dotenv import load_dotenv
from loguru import logger

# Import the skill to be tested
from skills.websearch import google_search

# Load environment variables from logfile
load_dotenv()

class test_search_for_python(unittest.TestCase):
    def test_python_search(self):
        result = google_search("Azure Functions backup to Azure Backup")

        print(result)

        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)
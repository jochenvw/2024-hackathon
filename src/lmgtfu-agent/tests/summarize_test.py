import unittest
import os
from dotenv import load_dotenv
from loguru import logger

# Import the skill to be tested
from skills.summarize import summarize_text

# Load environment variables from logfile
load_dotenv()

class test_summarization(unittest.TestCase):

    def test_summarize_text(self):
        # Read the long text from a file 'long_txt.md' (thanks ChatGPT for the text)
        # and summarize it in 1 sentence - asserts that the result is not None        
        with open("tests/long_txt.md", "r") as f:
            long_text = f.read()
            result = summarize_text("summarize in 1 sentence", long_text)

            print(result)

            self.assertIsNotNone(result)
            self.assertGreater(len(result), 0)
            self.assertLessEqual(len(result), 1000)
import unittest
from dotenv import load_dotenv
from loguru import logger

# Import the skill to be tested
from skills.get_arm_spec import go_get_arm_spec

# Load environment variables from logfile
load_dotenv()

class test_arm_spec_getter(unittest.TestCase):

    def test_get_arm_template(self):
        # Scrape the content of a website and summarize it - asserts that the result is not None
        result = go_get_arm_spec("Azure web app")

        print(result)
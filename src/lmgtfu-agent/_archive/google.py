from autogen.coding.func_with_reqs import with_requirements
import requests
from typing import List, Tuple, Optional

# Define the structure of a search result entry
ResponseEntry = Tuple[str, str, str]

@with_requirements(python_packages=["requests"], global_imports=["typing"])
def SearchGoogle(self, query: str, cnt: int) -> Optional[List[ResponseEntry]]:
        """
        Performs a Google search and processes the results.
        Parameters:
        - query (str): The search query string.
        - cnt (int): The number of search results to return.

        Returns:
        - A list of ResponseEntry tuples containing the title, URL, and snippet of each Google search result.
        """
        api_key = "AIzaSyDwD24GoicfSRWIUyXjV-o5CoxMyd_ur5s",
        search_engine_id = "55c057e0e696749cb",
        url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={query}"
        if cnt > 0:
            url += f"&num={cnt}"
        response = requests.get(url)
        if response.status_code == 200:
            result_list: List[ResponseEntry] = []
            for item in response.json().get("items", []):
                result_list.append((item["title"], item["link"], item["snippet"]))
            return result_list
        else:
            print(f"Error with Google Custom Search API: {response.status_code}")
            return None
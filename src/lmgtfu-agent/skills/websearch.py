import json
import os
import requests


def google_search(search_keyword : str) -> str:    
    """
    Perform a Google search using the Serper API.
    Args:
        search_keyword (str): The keyword or query to search for.
    Returns:
        str: The response text from the Serper API containing the search results.
    Raises:
        requests.exceptions.RequestException: If there is an issue with the HTTP request.
    Example:
        >>> result = google_search("Python programming")
        >>> print(result)
    """
    url = "https://google.serper.dev/search"

    payload = json.dumps({
        "q": search_keyword
    })

    headers = {
        'X-API-KEY': os.getenv("SERPER_API_KEY"),
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print("RESPONSE:", response.text)
    return response.text
import json
import os
import requests


def google_search(search_keyword: str, site: str = "") -> list[str]:    
    """
    Perform a Google search using the Serper API.
    Args:
        search_keyword (str): The keyword or query to search for.
        site (str, optional): The site to restrict the search to. Defaults to "".
    Returns:
        list[str]: A list of URLs from the search results.
    Raises:
        requests.exceptions.RequestException: If there is an issue with the HTTP request.
    Example:
        >>> result = google_search("Python programming")
        >>> print(result)
    """
    url = "https://google.serper.dev/search"

    query = search_keyword
    if site:
        query += f" site:{site}"

    payload = json.dumps({
        "q": query
    })

    headers = {
        'X-API-KEY': os.getenv("SERPER_API_KEY"),
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(f'Searching Google for {search_keyword}...')

    data = response.json()

    # The result is a JSON object with a property 'organic' that contains the search results
    # inside, there's a link to the search result. That's the only thing we're interested in.
    links = [entry['link'] for entry in data['organic']]
    return links
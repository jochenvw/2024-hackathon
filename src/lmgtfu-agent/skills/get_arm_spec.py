from langchain_core.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI
from langchain.chains import LLMChain
import json
import os

from skills.websearch import google_search
from skills.scrape_website import scrape_website

def go_get_arm_spec(serviceName: str) -> str:
    """
    Retrieves the Azure Resource Manager (ARM) specification URL for a given Azure service.
    This function performs the following steps:
    1. Conducts a Google search to find URLs related to the ARM templates on the Microsoft Learn site.
    2. Uses an Azure OpenAI model to filter and identify the most relevant URL that contains the ARM template for the specified service.
    3. Scrapes the identified URL to retrieve the ARM specification.
    4. Summarizes the retrieved ARM specification text.
    Args:
        serviceName (str): The name of the Azure service for which the ARM specification is needed.
    Returns:
        str: A summarized text of the ARM specification for the specified service.
    """
    armSpecSite = "learn.microsoft.com/en-us/azure/templates"
    searchResults = google_search(serviceName, armSpecSite)

    print(f"Found {len(searchResults)} search results for {serviceName} on {armSpecSite}")

    endpoint = os.getenv("OAI_ENDPOINT")
    key = os.getenv("OAI_KEY")
    api_version = os.getenv("OAI_VERSION")

    llm = AzureChatOpenAI(temperature = 0, model = "gpt-4-32k", azure_endpoint=endpoint, api_key=key, api_version=api_version)
    
    # Selec the URL from the list of search results
    tpl = """
        In the list of URLs, find the best best candidate to contain information about {service_name}. 
        - Return the URL that contains the Azure Resource Provider name of the Azure service name
        - Otherwise, return the URL that contains the service name 
        - Ensure to point to the URL that contains the ARM template for the service, by including URL Query Parameters "?pivots=deployment-language-arm-template"
        - Respond with the URL and only the URL

        ## begin list of URLs

        {searchResults}

        ## end list of URLs
    """
    filter_tpl = PromptTemplate(template=tpl, input_variables=["service_name", "searchResults"])   

    filter_chain = filter_tpl | llm
    
    inputs = {
        "service_name": serviceName,
        "searchResults": json.dumps(searchResults)
    }
    
    output = filter_chain.invoke(inputs)

    print(f"Identified the best URL for {serviceName}: {output.content}")
    url = output.content
    armSpec = scrape_website(url=url, objective="summarize to be used to generate an ARM template. So keep all JSON properties, descriptions and examples.", summarizeText=False)


    # Selec the URL from the list of search results
    tpl = """
        Filter out the ARM specification page and ONLY return the 'Resource format' part, which contains the JSON schema for the ARM template.

        ## begin of documentation
        {documentation}
        ## end of documentation
    """
    filter_tpl = PromptTemplate(template=tpl, input_variables=["documentation"])   
    filter_chain = filter_tpl | llm
    
    inputs = {
        "documentation": armSpec,
    }

    resource_format = filter_chain.invoke(inputs)

    result = {
        "serviceName": serviceName,
        "url": url,
        "resource_format": resource_format.content,
        "raw_arm_spec": armSpec
    }

    return result
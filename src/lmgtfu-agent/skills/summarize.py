from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain_openai import AzureChatOpenAI
import os

def summarize_text(objective: str, content: str) -> str:
    """
    Summarizes the given content based on the specified objective.
    Args:
        objective (str): The objective or purpose for which the summary is being created.
        content (str): The text content that needs to be summarized.
    Returns:
        str: The summarized text.
    Environment Variables:
        OAI_ENDPOINT (str): The endpoint for the OpenAI API.
        OAI_KEY (str): The API key for accessing the OpenAI API.
        OAI_VERSION (str): The version of the OpenAI API to use.
    Raises:
        ValueError: If the environment variables for the OpenAI API are not set.
    """        

    endpoint = os.getenv("OAI_ENDPOINT")
    key = os.getenv("OAI_KEY")
    api_version = os.getenv("OAI_VERSION")

    llm = AzureChatOpenAI(temperature = 0, model = "gpt-4-32k", azure_endpoint=endpoint, api_key=key, api_version=api_version)

    text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n"], chunk_size = 10000, chunk_overlap=500)
    docs = text_splitter.create_documents([content])
    
    map_prompt = """
        Write a summary of the following text for {objective}:
        "{text}"
        SUMMARY:
    """
    map_prompt_template = PromptTemplate(template=map_prompt, input_variables=["text", "objective"])
    
    summary_chain = load_summarize_chain(
        llm=llm, 
        chain_type='map_reduce',
        map_prompt = map_prompt_template,
        combine_prompt = map_prompt_template,
        verbose = False
    )

    # input dictionary
    inputs = {
        "input_documents": docs,
        "objective": objective
    }
    
    output = summary_chain.invoke(inputs)
    return output
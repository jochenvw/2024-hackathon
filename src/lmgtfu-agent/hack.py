#    ___   ____ ___  __ __     __  __           __         __  __              
#   |__ \ / __ \__ \/ // /    / / / /___ ______/ /______ _/ /_/ /_  ____  ____ 
#   __/ // / / /_/ / // /_   / /_/ / __ `/ ___/ //_/ __ `/ __/ __ \/ __ \/ __ \
#  / __// /_/ / __/__  __/  / __  / /_/ / /__/ ,< / /_/ / /_/ / / / /_/ / / / /
# /____/\____/____/ /_/    /_/ /_/\__,_/\___/_/|_|\__,_/\__/_/ /_/\____/_/ /_/ 
#
# Project page: https://hackbox.microsoft.com/hackathons/hackathon2024/project/73988
# Repository:   https://github.com/jochenvw/2024-hackathon
#
# Hackers:
# Nikita Dandwani
# Dylan de Jong
# Arthur Hallensleben
# Krishnan Subramanian
# Naveen Kumar Selvaraj
# Prakash Palanisami
# Jochen van Wylick
#
# Lot of inspiration from: https://github.com/JayZeeDesign/research-agents-3.0/blob/main/app.py

import autogen
from autogen import UserProxyAgent
from autogen.agentchat.contrib.gpt_assistant_agent import GPTAssistantAgent
from autogen import register_function

from dotenv import load_dotenv

# Reads the .env file and loads the environment variables
# use with os.getenv("VAR_NAME")
load_dotenv()

# Load the skills
from skills.websearch import google_search
from skills.scrape_website import scrape_website
from skills.summarize import summarize_text


config_list_gpt4 = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": ["gpt-4-32k"],
    },
)

gpt4_config = {
    "cache_seed": 42,  # change the cache_seed for different trials
    "temperature": 0,
    "config_list": config_list_gpt4,
    "timeout": 120,
}

user_proxy = UserProxyAgent(name="user_proxy",
    is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
    human_input_mode="ALWAYS",
    max_consecutive_auto_reply=1
)

researcher = autogen.AssistantAgent(
    name = "researcher",
    system_message="Researcher. You can search the web and when you find relevant links from trustworthy sources, you can scrape the URL carefully and summarize the content.",
    llm_config = {
        "config_list": config_list_gpt4,
    },
)

executor = autogen.UserProxyAgent(
    name="executor",
    system_message="Executor. Execute the code requested by the researcher and report the result back to the researcher",
    human_input_mode="NEVER",
    code_execution_config={
        "last_n_messages": 3,
        "work_dir": "paper",
        "use_docker": False,
    },  
)

register_function(scrape_website, caller=researcher, executor=executor, name="web_scraping", description="A tool to scrape website contents", )
register_function(google_search, caller=researcher, executor=executor, name="google_search", description="A tool to search the internet or web for a specific topic", )

research_manager = autogen.AssistantAgent(
    name="research_manager",
    system_message="Research Manager. You can assign tasks to researchers and summarize the results. You create a plan based on the input from the user_proxy and are also responsible for presenting the results back to the user_proxy.",
    llm_config = {
        "config_list": config_list_gpt4,
    }
)

# Create group chat
groupchat = autogen.GroupChat(agents=[user_proxy, researcher, research_manager, executor], messages=[], max_round=15)
group_chat_manager = autogen.GroupChatManager(groupchat=groupchat, llm_config={"config_list": config_list_gpt4})


message = """
You are an expert in Azure services and their integrations with Azure KeyVault. Please check whether each of the following Azure services can be backed up using Azure KeyVault. Return the results in a markdown table with the following columns:

- **Service Name**: The name of the Azure service.
- **Can Be Backed Up with KeyVault**: Yes or No.
- **Backup Method**: If Yes, explain the backup method. If No, explain why it can't be backed up using KeyVault.

Here is the list of Azure services to check:

- Azure Blob Storage
- Azure SQL Database
- Azure App Service
- Azure Virtual Machines
- Azure Kubernetes Service (AKS)
- Azure Cosmos DB

Return the results in a properly formatted markdown table.
"""
user_proxy.initiate_chat(group_chat_manager, message=message)
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

# Load the agents
from agents import prompt_engineer, researcher, research_manager, executor, user_proxy, result_critic, waf_expert

config_list_gpt4 = autogen.config_list_from_json("OAI_CONFIG_LIST")

gpt4_config = {
    "cache_seed": 42,  # change the cache_seed for different trials
    "temperature": 0,
    "config_list": config_list_gpt4,
    "timeout": 120,
}

#register_function(scrape_website, caller=researcher.agent, executor=executor.agent, name="web_scraping", description="A tool to get the contents from of a specific URL of a website", )
#register_function(google_search, caller=researcher.agent, executor=executor.agent, name="google_search", description="A tool to search the internet or web for a specific topic", )
#register_function(scrape_website, caller=result_critic.agent, executor=executor.agent, name="web_scraping", description="A tool to get the contents from of a specific URL of a website", )


# Create group chat
groupchat = autogen.GroupChat(agents=[user_proxy.agent, prompt_engineer.agent, researcher.agent, research_manager.agent, executor.agent, result_critic.agent, waf_expert.agent], messages=[], max_round=100)
group_chat_manager = autogen.GroupChatManager(groupchat=groupchat, llm_config={"config_list": config_list_gpt4})


message = """
Generate for me the ARM template to enable CMK for Azure NetApp Files.  
"""
user_proxy.agent.initiate_chat(group_chat_manager, message=message)
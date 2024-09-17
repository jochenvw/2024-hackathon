import autogen
config_list_gpt4 = autogen.config_list_from_json("OAI_CONFIG_LIST")

researcher_prompt = """
Researcher. 
You can search the web and when you find relevant links from trustworthy sources, you can scrape the URL carefully and summarize the content.
"""

agent = autogen.AssistantAgent(
    name = "researcher",
    system_message=researcher_prompt,
    llm_config = {
        "config_list": config_list_gpt4,
    },
)

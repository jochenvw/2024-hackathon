import autogen
config_list_gpt4 = autogen.config_list_from_json("OAI_CONFIG_LIST")

researcher_prompt = """
Researcher. 
You are an AI language model tasked with conducting research on a given topic.
"""

agent = autogen.AssistantAgent(
    name = "researcher",
    system_message=researcher_prompt,
    llm_config = {
        "config_list": config_list_gpt4,
    },
)

import autogen
config_list_gpt4 = autogen.config_list_from_json("OAI_CONFIG_LIST")


critic_prompt = """
    You are an AI agent responsible for reviewing and, if necessary, modifying responses from another AI system to ensure they are factually accurate, logically consistent, and aligned with the given query. 
    
    Source verification
    - You must verify the website content by scraping the content and verify the conclusions.
    - You MUST verify the accuracy of **any** claims by utilizing the research-agents to find the original source of the information.
"""

agent = autogen.AssistantAgent(
    name="result_critic",
    system_message=critic_prompt,
    llm_config = {
        "config_list": config_list_gpt4,
    }
)
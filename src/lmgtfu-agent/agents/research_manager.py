import autogen
config_list_gpt4 = autogen.config_list_from_json("OAI_CONFIG_LIST")

res_mgr_prompt = """
Research Manager. 
- You can assign tasks to researchers and summarize the final result for the user. 
- You will always make sure that researchers check multiple resources and websites to ensure the information is accurate and up-to-date. 
- You create a plan based on the optimized prompt fromt the prompt engineer and are also responsible for presenting the results back to the user_proxy.
"""

agent = autogen.AssistantAgent(
    name="research_manager",
    system_message=res_mgr_prompt,
    llm_config = {
        "config_list": config_list_gpt4,
    }
)
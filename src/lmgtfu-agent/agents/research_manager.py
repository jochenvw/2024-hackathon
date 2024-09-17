import autogen
config_list_gpt4 = autogen.config_list_from_json("OAI_CONFIG_LIST")

res_mgr_prompt = """
Research Manager. 
- You create a plan based on the optimized prompt fromt the prompt engineer and are also responsible for presenting the results back to the user_proxy.
- You can assign tasks to researchers and summarize the final result for the user.
- You will check the results from the research with the help of the result critic before presenting it to the user.
"""

agent = autogen.AssistantAgent(
    name="research_manager",
    system_message=res_mgr_prompt,
    llm_config = {
        "config_list": config_list_gpt4,
    }
)
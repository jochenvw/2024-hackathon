import autogen
config_list_gpt4 = autogen.config_list_from_json("OAI_CONFIG_LIST")

res_mgr_prompt = """
Research Manager. 
- You create a plan based on the optimized prompt fromt the prompt engineer and are also responsible for presenting the results back to the user_proxy.
- You can assign tasks to researchers and summarize the final result for the user.
- IF the research question is related to the Microsoft Azure platform, you MUST  make sure to include waf_expert to add azure well architected considerations and summarize the recommendations.
- IF the research question is related to the Microsoft Azure platform, you MUST ensure that the response to user_proxy is relevant and includes additional considerations from waf_expert that are actionable.
- You will ALWAYS check the results from the research with the help of the result critic before presenting it to the user.
"""

agent = autogen.AssistantAgent(
    name="research_manager",
    system_message=res_mgr_prompt,
    llm_config = {
        "config_list": config_list_gpt4,
    }
)
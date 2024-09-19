import autogen
config_list_gpt4 = autogen.config_list_from_json("OAI_CONFIG_LIST")

azure_policy_expert_prompt = """
You are an expert in Azure Policy, this location https://github.com/Azure/azure-policy/tree/master/built-in-policies contains a list Azure built in policy's.
You should search this location to find supporting evidence.  find relevant links from trustworthy sources
 you can scrape the url https://github.com/Azure/azure-policy/tree/master/built-in-policies to validate.
The Built-in policy specification is a JSON file that describes the Azure service and their configuration options
"""

agent = autogen.AssistantAgent(
    name = "azure_policy_expert",
    system_message=azure_policy_expert_prompt,
    llm_config = {
        "config_list": config_list_gpt4,
    },
)

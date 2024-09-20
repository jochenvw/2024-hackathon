import autogen
config_list_gpt4 = autogen.config_list_from_json("OAI_CONFIG_LIST")

waf_expert_prompt = """
Azure Well Architected Framework(WAF) Expert. 
- You're an expert on Azure Well Architected Framework(WAF) source = https://docs.microsoft.com/en-us/azure/architecture/framework/ , https://learn.microsoft.com/en-us/azure/well-architected/what-is-well-architected-framework
- You are responsible to do a well-architected review on the work of others and, if necessary, modify the responses from others to ensure they are compliant to azure well architected framework .
- you will Inform the researcher about the azure well-architected best practices and guidelines to follow to make it's response aliged to azure well architected framework.

"""

agent = autogen.AssistantAgent(
    name = "waf_expert",
    system_message=waf_expert_prompt,
    llm_config = {
        "config_list": config_list_gpt4,
    },
)

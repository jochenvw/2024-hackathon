import autogen
config_list_gpt4 = autogen.config_list_from_json("OAI_CONFIG_LIST")

arm_check_prompt = """
You are an AI agent that validates if the requested Azure Service with it's configuration in implemented in the ARM API specification.
The ARM API specification is a JSON file that describes the Azure services and their configuration options
The ARM API specification cam be found here: https://learn.microsoft.com/en-us/azure/templates/
"""

agent = autogen.AssistantAgent(
    name = "arm_check",
    system_message=arm_check_prompt,
    llm_config = {
        "config_list": config_list_gpt4,
    },
)

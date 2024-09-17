import autogen
config_list_gpt4 = autogen.config_list_from_json("OAI_CONFIG_LIST")

agent = autogen.UserProxyAgent(name="user_proxy",
    is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
    human_input_mode="ALWAYS",
    max_consecutive_auto_reply=1
)
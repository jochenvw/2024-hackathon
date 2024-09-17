import autogen
config_list_gpt4 = autogen.config_list_from_json("OAI_CONFIG_LIST")

agent = autogen.UserProxyAgent(
    name="executor",
    system_message="Executor. Execute the code requested by the researcher and report the result back to the researcher",
    human_input_mode="NEVER",
    code_execution_config={
        "last_n_messages": 3,
        "work_dir": "paper",
        "use_docker": False,
    },  
)
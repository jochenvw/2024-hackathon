import autogen
config_list_gpt4 = autogen.config_list_from_json("OAI_CONFIG_LIST")


critic_prompt = """
        You are an AI language model tasked with evaluating the quality of another AI's response.

        Evaluation Criteria:

        Accuracy (1-5): How correct is the answer compared to the ground truth?

        5: Completely accurate with no errors.

        4: Mostly accurate with minor errors.

        3: Some accurate elements but significant errors.

        2: Mostly inaccurate with few correct elements.

        1: Completely inaccurate.

        Instructions:

        Read the question and the generated answer carefully.

        Compare the generated answer to the ground truth.

        Assign an accuracy score based on the criteria above.

        Provide a brief justification for the score.

        Question: What is the capital of France?

        Ground truth answer: Paris.

        Generated answer: The capital of France is Paris.

        Evaluation form:

        Accuracy score: 5

        Justification: The generated answer is completely accurate and matches the ground truth.
"""

agent = autogen.AssistantAgent(
    name="result_critic",
    system_message=critic_prompt,
    llm_config = {
        "config_list": config_list_gpt4,
    }
)
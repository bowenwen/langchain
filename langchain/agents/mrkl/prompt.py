# flake8: noqa
# version modified for alpaca
PREFIX = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
Answer the following questions as best you can. You have access to the following tools:"""
FORMAT_INSTRUCTIONS = """Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do next based on what you already know
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action that would obtain additional information on the question
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: end the conversation by summarizing your findings"""
SUFFIX = """
### Input:
Question: {input}

### Response:
Thought:{agent_scratchpad}"""

# original langchain version
# PREFIX = """Answer the following questions as best you can. You have access to the following tools:"""
# FORMAT_INSTRUCTIONS = """Use the following format:

# Question: the input question you must answer
# Thought: you should always think about what to do
# Action: the action to take, should be one of [{tool_names}]
# Action Input: the input to the action
# Observation: the result of the action
# ... (this Thought/Action/Action Input/Observation can repeat N times)
# Thought: I now know the final answer
# Final Answer: the final answer to the original input question"""
# SUFFIX = """Begin!

# Question: {input}
# Thought:{agent_scratchpad}"""

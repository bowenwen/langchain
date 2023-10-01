# flake8: noqa
from langchain.prompts import PromptTemplate

prompt_template = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
Write a concise summary of the input text.

### Input:
"{text}"

### Response:"""
PROMPT = PromptTemplate(template=prompt_template, input_variables=["text"])

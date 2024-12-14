from langchain_core.language_models import BaseLLM
from langchain_core.prompts import PromptTemplate


class TemplatedGenerator:
    prompt_template: str
    prompt: PromptTemplate
    llm: BaseLLM

    def __init__(self, llm, prompt_template: str):
        self.llm = llm
        self.prompt_template = prompt_template
        self.prompt = PromptTemplate.from_template(template=prompt_template)

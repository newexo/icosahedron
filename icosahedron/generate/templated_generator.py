from langchain_core.prompts import PromptTemplate

from .model_context import ModelContext


class TemplatedGenerator:
    prompt_template: str
    prompt: PromptTemplate
    context: ModelContext

    def __init__(self, prompt_template: str, context: ModelContext = None):
        self.context = context
        self.llm = context.get_llm()
        self.prompt_template = prompt_template
        self.prompt = PromptTemplate.from_template(template=prompt_template)
from langchain_core.prompts import PromptTemplate

from .model_context import ModelContext


class TemplatedGenerator:
    prompt_template: str
    prompt: PromptTemplate
    context: ModelContext
    verbose: bool = False

    def __init__(self, prompt_template: str, context: ModelContext = None, verbose: bool = False):
        self.context = context
        self.llm = context.get_llm()
        self.prompt_template = prompt_template
        self.prompt = PromptTemplate.from_template(template=prompt_template)
        self.verbose = verbose

    def prompt_formatted_str(self, **kwargs) -> str:
        return self.prompt.format(**kwargs)

    def generate(self, **kwargs):
        prompt_formatted_str: str = self.prompt_formatted_str(**kwargs)
        result = self.llm.invoke(prompt_formatted_str)
        if self.verbose:
            print(result)
        return self.context.interpret_json_result(result)

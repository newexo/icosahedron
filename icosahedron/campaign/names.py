from langchain_core.language_models.llms import BaseLLM
from langchain.prompts import PromptTemplate

from ..directories import templates

with open(templates("name_prompt_template.txt")) as f:
    default_name_prompt_template = f.read()


class NameGenerator:
    prompt_template: str
    prompt: PromptTemplate
    llm: BaseLLM

    def __init__(self, llm, prompt_template: str = default_name_prompt_template):
        self.llm = llm
        self.prompt_template = prompt_template
        self.prompt = PromptTemplate.from_template(template=prompt_template)

    def prompt_formatted_str(self, culture, number, gender) -> str:
        return self.prompt.format(culture=culture, number=number, gender=gender)

    def generate(
        self,
        culture: str = "European high fantasy",
        number: int = 30,
        gender: str = "male",
    ):
        prompt_formatted_str: str = self.prompt_formatted_str(
            culture=culture, number=number, gender=gender
        )
        return self.llm.invoke(prompt_formatted_str)

from langchain_core.language_models.llms import BaseLLM
from langchain.prompts import PromptTemplate

default_name_prompt_template = """You are a GM of am RPG. You are creating campaign and need to create 
a list of names for potential NPCs and player characters. The campaign is set in a culture 
similar to {culture}. List {number} suggested names with etymology for {gender} characters.
express the results as a JSON list of objects with fields `name`, `etymology` (a sentence 
explaining the historical origin of the name as word), `origin` 
(language or nationality) and `gender` 
(male, female and any). Display only a JSON object with no other text."""


class NameGenerator:
    prompt_template: str
    prompt: PromptTemplate
    llm: BaseLLM

    def __init__(self, llm, prompt_template: str = default_name_prompt_template):
        self.llm = llm
        self.prompt_template = prompt_template
        self.prompt = PromptTemplate.from_template(template=prompt_template)

    def generate(
        self,
        culture: str = "European high fantasy",
        number: int = 30,
        gender: str = "male",
    ):
        prompt_formatted_str: str = self.prompt.format(
            culture=culture, number=number, gender=gender
        )
        return self.llm.invoke(prompt_formatted_str)

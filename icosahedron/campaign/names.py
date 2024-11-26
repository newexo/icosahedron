from langchain_core.language_models.llms import BaseLLM
from langchain.prompts import PromptTemplate

default_name_prompt_template = """
You are a GM of an RPG. You are creating a campaign and need to generate a list of names 
for potential NPCs and player characters. The campaign is set in a culture similar to {culture}. 
Provide {number} suggested names with etymology for {gender} characters. Express the results 
as a JSON list of objects with the following fields: 
- `name` (the name itself)
- `etymology` (a sentence explaining the historical origin of the name as a word)
- `origin` (language or nationality)
- `gender` (male, female, or any).

Display only the JSON list of objects with no additional text.
"""


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

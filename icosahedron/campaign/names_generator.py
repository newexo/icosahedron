from ..generate.templated_generator import TemplatedGenerator
from ..generate.model_context import ModelContext
from ..directories import templates

with open(templates("name_prompt_template.txt")) as f:
    default_name_prompt_template = f.read()


class NameGenerator(TemplatedGenerator):
    def __init__(
        self,
        context: ModelContext,
        prompt_template: str = default_name_prompt_template,
    ):
        super().__init__(prompt_template=prompt_template, context=context)

    def generate(
        self,
        culture: str = "European high fantasy",
        number: int = 30,
        gender: str = "male",
    ):
        return super().generate(culture=culture, number=number, gender=gender)

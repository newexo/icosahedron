from icosahedron.generate.model_context import ModelContext
from icosahedron.directories import templates
from icosahedron.generate.templated_generator import TemplatedGenerator


with open(templates("magic_ring_list.txt")) as f:
    default_magic_ring_list_template = f.read()


class RingNameGenerator(TemplatedGenerator):
    def __init__(
        self,
        context: ModelContext,
        prompt_template: str = default_magic_ring_list_template,
    ):
        super().__init__(prompt_template=prompt_template, context=context)

    def generate(
        self,
        culture: str = "European high fantasy",
        number: int = 30,
    ):
        prompt_formatted_str: str = self.prompt_formatted_str(
            culture=culture, number=number
        )
        result = self.llm.invoke(prompt_formatted_str)
        return self.context.interpret_json_result(result)


with open(templates("magic_ring_template.txt")) as f:
    default_magic_ring_template = f.read()


class RingDetailsGenerator(TemplatedGenerator):
    def __init__(
            self,
            context: ModelContext,
            prompt_template: str = default_magic_ring_template,
    ):
        super().__init__(prompt_template=prompt_template, context=context)

    def generate(
            self,
            culture: str = "European high fantasy",
            name: str = "Ring of Invisibility",
    ):
        prompt_formatted_str: str = self.prompt_formatted_str(
            culture=culture, name=name
        )
        result = self.llm.invoke(prompt_formatted_str)
        return self.context.interpret_json_result(result)
from abc import ABCMeta, abstractmethod

import openai


class Generator(metaclass=ABCMeta):
    def __init__(
        self,
        name,
        delimiter="####",
        model="gpt-3.5-turbo",
        temperature=0,
        max_tokens=500,
    ):
        self.name = name
        self.delimiter = delimiter
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

    @abstractmethod
    def _make_system_message(self):
        pass

    def _make_user_message(self):
        return f"Write a JSON object for {self.delimiter}{self.name}{self.delimiter}."

    @property
    def system_message(self):
        return self._make_system_message()

    @property
    def user_message(self):
        return self._make_user_message()

    def _make_messages(self):
        return [
            {"role": "system", "content": self.system_message},
            {"role": "user", "content": self.user_message},
        ]

    @property
    def messages(self):
        return self._make_messages()

    def generate(self):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages,
            temperature=self.temperature,
        )
        return response.choices[0].message["content"]


class GeneratorFromExample(Generator):
    def __init__(
        self,
        name,
        json_sample,
        delimiter="####",
        model="gpt-3.5-turbo",
        temperature=0,
        max_tokens=500,
    ):
        super().__init__(name, delimiter, model, temperature, max_tokens)
        self.json_sample = json_sample

    def _make_system_message(self):
        return f"""You are a developer for software implementation of a fantasy RPG. \
You are adding entries to database of adventuring equipment. \
The name of the equipment item to implement will be delimited with \
{self.delimiter} characters.
Output a JSON objects, where each object is like the following example: \
{self.json_sample} \
 \
Only JSON objects, with nothing else."""


class GeneratorArmor(GeneratorFromExample):
    def __init__(
        self, name, delimiter="####", model="gpt-3.5-turbo", temperature=0, max_tokens=500
    ):
        json_sample = """{ \
    "name": "Chain Mail", \
    "weight": 40, \
    "description": "Chain Mail Armor is made up of thousands of interlinked metal rings, forming a flexible mesh-like structure that drapes over your body to provide protection. The intricate web of these interlocking rings not only absorbs the impact of attacks but also allows for some degree of movement and flexibility, despite its weight and bulkiness.", \
    "condition": "new", \
    "value": 75, \
    "armor_class": 16, \
    "max_dex_bonus": 2, \
    "check_penalty": -5, \
    "spell_failure": 30, \
    "speed_reduction": 10 \
}"""
        super().__init__(name, json_sample, delimiter, model, temperature, max_tokens)

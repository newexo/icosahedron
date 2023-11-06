from abc import ABCMeta, abstractmethod

import openai

import json
from icosahedron import directories

with open(directories.data("example_items.json")) as f:
    example_items = json.load(f)


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
        return example_items["item_system_message"].format(self.delimiter, self.json_sample)


class GeneratorArmor(GeneratorFromExample):
    def __init__(
        self, name, delimiter="####", model="gpt-3.5-turbo", temperature=0, max_tokens=500
    ):
        json_sample = json.dumps(example_items["chain_mail"], indent=4)
        super().__init__(name, json_sample, delimiter, model, temperature, max_tokens)

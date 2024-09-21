from abc import ABCMeta, abstractmethod

import openai
import datetime
import asyncio

from enum import Enum

import json
from icosahedron import directories

with open(directories.data("example_items.json")) as f:
    example_items = json.load(f)


class ModelContext:
    client: openai.OpenAI
    delimiter: str
    model: str
    temperature: float
    max_tokens: int

    def __init__(
        self,
        client: openai.OpenAI,
        delimiter: str = None,
        model: str = None,
        temperature: float = 0.0,
        max_tokens: int = -1,
    ):
        self.client = client
        if delimiter is None:
            delimiter = "####"
        self.delimiter = delimiter
        if model is None:
            model = self._default_gpt3_5_turbo()
        self.model = model
        self.temperature = temperature
        if max_tokens < 0:
            max_tokens = 500
        self.max_tokens = max_tokens

    @staticmethod
    def _default_gpt3_5_turbo():
        return "gpt-4o"


class Generator(metaclass=ABCMeta):
    def __init__(
        self,
        name: str,
        context: ModelContext = None,
    ):
        self.name = name
        if context is None:
            context = ModelContext(client=openai.OpenAI())
        self.context = context

    @abstractmethod
    def _make_system_message(self):
        pass

    def _make_user_message(self):
        return (
            f"Write a JSON object for {self.context.delimiter}{self.name}{self.context.delimiter}. Do produce any "
            f"other output besides the JSON."
        )

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
        response = self.context.client.chat.completions.create(
            model=self.context.model,
            messages=self.messages,
            temperature=self.context.temperature,
        )
        content = response.choices[0].message.content.strip()
        return json.loads(content)


class ExampleItemType(Enum):
    ARMOR = "chain_mail"
    WEAPON = "mace"
    MAGIC_RING = "ring_of_protection"
    GENERIC_ITEM = "spellbook"


class GeneratorFromExample(Generator):
    def __init__(
        self,
        name: str,
        context: ModelContext = None,
        json_sample: str = None,
        dictionary_sample: dict = None,
    ):
        super().__init__(name, context)
        if json_sample is None:
            json_sample = json.dumps(dictionary_sample, indent=4)
        self.json_sample = json_sample

    def _make_system_message(self):
        return example_items["item_system_message"].format(
            self.context.delimiter, self.json_sample
        )

    @staticmethod
    def get_generator(t: ExampleItemType, name: str, context: ModelContext = None):
        return GeneratorFromExample(
            name, context, dictionary_sample=example_items[t.value]
        )

    @classmethod
    async def generate_items(
        cls, t: ExampleItemType, names, context: ModelContext = None
    ):
        async def generate_item(name):
            return cls.get_generator(t, name, context).generate()

        tasks = [asyncio.create_task(generate_item(name)) for name in names]
        results = asyncio.gather(*tasks)

        return await results

from abc import ABCMeta, abstractmethod

import openai
import datetime

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
        # expected deprecation date on 2024-06-12
        current_date = datetime.datetime.now().date()
        target_date = datetime.date(2024, 6, 12)

        if current_date > target_date:
            return "gpt-3.5-turbo"
        else:
            return "gpt-3.5-turbo-0301"


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
        return f"Write a JSON object for {self.context.delimiter}{self.name}{self.context.delimiter}."

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
        return response.choices[0].message.content.strip()


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


class GeneratorArmor(GeneratorFromExample):
    def __init__(
        self,
        name: str,
        context: ModelContext = None,
    ):
        super().__init__(
            name,
            context,
            dictionary_sample=example_items["chain_mail"],
        )


class GeneratorWeapon(GeneratorFromExample):
    def __init__(
        self,
        name: str,
        context: ModelContext = None,
    ):
        super().__init__(
            name,
            context,
            dictionary_sample=example_items["mace"],
        )


class GeneratorMagicRing(GeneratorFromExample):
    def __init__(
        self,
        name: str,
        context: ModelContext = None,
    ):
        super().__init__(
            name,
            context,
            dictionary_sample=example_items["ring_of_protection"],
        )


class GeneratorGenericItem(GeneratorFromExample):
    def __init__(
        self,
        name: str,
        context: ModelContext = None,
    ):
        super().__init__(
            name,
            context,
            dictionary_sample=example_items["spellbook"],
        )

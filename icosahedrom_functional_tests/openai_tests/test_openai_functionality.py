import pytest
import asyncio

import os

from icosahedron.env import load_icosahedron_env
from icosahedron.generate.generate_from_example import (
    GeneratorFromExample,
    ExampleItemType,
)


pytest_plugins = ('pytest_asyncio',)


@pytest.fixture
def load_env():
    load_icosahedron_env()


def test_openai_key_exists(load_env):
    assert os.getenv("OPENAI_ORGANIZATION")
    assert os.getenv("OPENAI_API_KEY")


def test_generate_armor(load_env):
    splint_mail = GeneratorFromExample.get_generator(
        ExampleItemType.ARMOR, "Splint Mail"
    ).generate()

    expected = {
        "name",
        "weight",
        "description",
        "condition",
        "value",
        "armor_class",
        "max_dex_bonus",
        "check_penalty",
        "spell_failure",
        "speed_reduction",
    }
    assert set(splint_mail.keys()) == expected

    assert splint_mail["name"] == "Splint Mail"
    assert type(splint_mail["weight"]) is int
    assert type(splint_mail["description"]) is str
    assert type(splint_mail["condition"]) is str
    assert type(splint_mail["value"]) is int
    assert type(splint_mail["armor_class"]) is int
    assert type(splint_mail["max_dex_bonus"]) is int
    assert type(splint_mail["check_penalty"]) is int
    assert type(splint_mail["spell_failure"]) is int
    assert type(splint_mail["speed_reduction"]) is int


@pytest.mark.asyncio
async def test_generate_items(load_env):
    armor_names = [
        "Leather Armor",
        "Studded Leather Armor",
        "Chain Shirt",
        "Splint Mail",
        "Banded Mail",
        "Plate Mail",
    ]
    armor_data = await GeneratorFromExample.generate_items(ExampleItemType.ARMOR, armor_names)
    assert len(armor_data) == len(armor_names)
    actual = {armor["name"] for armor in armor_data}
    assert actual == set(armor_names)

import pytest
import json
from icosahedron.d20_rules.spells import Spell
from icosahedron.directories import test_data


@pytest.fixture
def spell():
    return Spell(
        name="Fireball",
        school="Evocation",
        level=3,
        casting_time="1 action",
        range_="Long (400 feet + 40 feet per caster level)",
        duration="Instantaneous",
        saving_throw="Reflex half",
        spell_resistance=True,
        components=["Verbal", "Somatic"],
        description="Conjures a fiery orb that explodes, dealing fire damage to all creatures and objects within a 20-foot radius. Affected creatures can make a Reflex saving throw for half damage.",
    )


@pytest.fixture
def instance_dict():
    with open(test_data("fireball.json")) as f:
        instance_str = f.read()
    return json.loads(instance_str)


def test_instance_test(spell):
    assert spell.name == "Fireball"
    assert spell.school == "Evocation"
    assert spell.level == 3
    assert spell.casting_time == "1 action"
    assert spell.range == "Long (400 feet + 40 feet per caster level)"
    assert spell.duration == "Instantaneous"
    assert spell.saving_throw == "Reflex half"
    assert spell.spell_resistance is True
    assert spell.components == ["Verbal", "Somatic"]
    assert (
        spell.description
        == "Conjures a fiery orb that explodes, dealing fire damage to all creatures and objects within a 20-foot radius. Affected creatures can make a Reflex saving throw for half damage."
    )


def test_from_dict(instance_dict):
    spell = Spell.from_dict(instance_dict)
    assert spell.name == "Fireball"
    assert spell.school == "Evocation"
    assert spell.level == 3
    assert spell.casting_time == "1 action"
    assert spell.range == "Long (400 feet + 40 feet per caster level)"
    assert spell.duration == "Instantaneous"
    assert spell.saving_throw == "Reflex half"
    assert spell.spell_resistance is True
    assert spell.components == ["Verbal", "Somatic"]
    assert (
        spell.description
        == "Conjures a fiery orb that explodes, dealing fire damage to all creatures and objects within a 20-foot radius. Affected creatures can make a Reflex saving throw for half damage."
    )

import pytest
import json
from icosahedron.d20_rules.feat import Feat
from icosahedron.directories import test_data


@pytest.fixture
def feat():
    name = "Spell Sniper"
    prerequisites = "Ability to cast at least one spell"
    benefit = "You have mastered ranged spells and gained the following benefits:\n- When you cast a spell that requires an attack roll, the spell's range is doubled.\n- Your ranged spell attacks ignore half and three-quarters cover.\n- You learn one cantrip that requires an attack roll. Choose the cantrip from any spellcasting class; your spellcasting ability for this cantrip depends on the class you selected."
    description = "The Spell Sniper feat enhances a character's spellcasting abilities and precision. It allows them to extend the range of their ranged spells, ignore cover when making spell attacks, and learn an additional attack roll-based cantrip from any spellcasting class."
    usage = "This feat's benefits apply whenever you cast a spell that requires an attack roll. The extended range and cover-ignoring effects are automatically in effect. To learn a new cantrip, consult the spellcasting rules for the chosen cantrip's spellcasting ability and other relevant details."
    normal_use = "Without the Spell Sniper feat, the character's ranged spells have their regular range and do not gain the benefits of extended range or cover-ignoring effects. The character's cantrip choices would follow the usual rules of their selected spellcasting class, without the additional attack roll-based cantrip granted by the feat."

    return Feat(
        name=name,
        prerequisites=prerequisites,
        benefit=benefit,
        description=description,
        usage=usage,
        normal_use=normal_use,
    )


@pytest.fixture
def instance_dict():
    with open(test_data("spell_sniper.json")) as f:
        instance_str = f.read()
    return json.loads(instance_str)


def test_instance_test(feat):
    name = "Spell Sniper"
    prerequisites = "Ability to cast at least one spell"
    benefit = "You have mastered ranged spells and gained the following benefits:\n- When you cast a spell that requires an attack roll, the spell's range is doubled.\n- Your ranged spell attacks ignore half and three-quarters cover.\n- You learn one cantrip that requires an attack roll. Choose the cantrip from any spellcasting class; your spellcasting ability for this cantrip depends on the class you selected."
    description = "The Spell Sniper feat enhances a character's spellcasting abilities and precision. It allows them to extend the range of their ranged spells, ignore cover when making spell attacks, and learn an additional attack roll-based cantrip from any spellcasting class."
    usage = "This feat's benefits apply whenever you cast a spell that requires an attack roll. The extended range and cover-ignoring effects are automatically in effect. To learn a new cantrip, consult the spellcasting rules for the chosen cantrip's spellcasting ability and other relevant details."
    normal_use = "Without the Spell Sniper feat, the character's ranged spells have their regular range and do not gain the benefits of extended range or cover-ignoring effects. The character's cantrip choices would follow the usual rules of their selected spellcasting class, without the additional attack roll-based cantrip granted by the feat."

    assert feat.name == name
    assert feat.prerequisites == prerequisites
    assert feat.benefit == benefit
    assert feat.description == description
    assert feat.usage == usage
    assert feat.normal_use == normal_use


def test_from_dict(instance_dict):
    feat = Feat.parse_obj(instance_dict)
    name = "Spell Sniper"
    prerequisites = "Ability to cast at least one spell"
    benefit = "You have mastered ranged spells and gained the following benefits:\n- When you cast a spell that requires an attack roll, the spell's range is doubled.\n- Your ranged spell attacks ignore half and three-quarters cover.\n- You learn one cantrip that requires an attack roll. Choose the cantrip from any spellcasting class; your spellcasting ability for this cantrip depends on the class you selected."
    description = "The Spell Sniper feat enhances a character's spellcasting abilities and precision. It allows them to extend the range of their ranged spells, ignore cover when making spell attacks, and learn an additional attack roll-based cantrip from any spellcasting class."
    usage = "This feat's benefits apply whenever you cast a spell that requires an attack roll. The extended range and cover-ignoring effects are automatically in effect. To learn a new cantrip, consult the spellcasting rules for the chosen cantrip's spellcasting ability and other relevant details."
    normal_use = "Without the Spell Sniper feat, the character's ranged spells have their regular range and do not gain the benefits of extended range or cover-ignoring effects. The character's cantrip choices would follow the usual rules of their selected spellcasting class, without the additional attack roll-based cantrip granted by the feat."

    assert feat.name == name
    assert feat.prerequisites == prerequisites
    assert feat.benefit == benefit
    assert feat.description == description
    assert feat.usage == usage
    assert feat.normal_use == normal_use

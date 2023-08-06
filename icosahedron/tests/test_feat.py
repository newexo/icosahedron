import unittest

from icosahedron.tests.base_test_case import BaseTestCase

from icosahedron.d20_rules.feat import Feat


class TestFeat(unittest.TestCase, BaseTestCase):
    def setUp(self):
        name = "Spell Sniper"
        prerequisites = "Ability to cast at least one spell"
        benefit = "You have mastered ranged spells and gained the following benefits:\n- When you cast a spell that requires an attack roll, the spell's range is doubled.\n- Your ranged spell attacks ignore half and three-quarters cover.\n- You learn one cantrip that requires an attack roll. Choose the cantrip from any spellcasting class; your spellcasting ability for this cantrip depends on the class you selected."
        description = "The Spell Sniper feat enhances a character's spellcasting abilities and precision. It allows them to extend the range of their ranged spells, ignore cover when making spell attacks, and learn an additional attack roll-based cantrip from any spellcasting class."
        usage = "This feat's benefits apply whenever you cast a spell that requires an attack roll. The extended range and cover-ignoring effects are automatically in effect. To learn a new cantrip, consult the spellcasting rules for the chosen cantrip's spellcasting ability and other relevant details."
        normal_use = "Without the Spell Sniper feat, the character's ranged spells have their regular range and do not gain the benefits of extended range or cover-ignoring effects. The character's cantrip choices would follow the usual rules of their selected spellcasting class, without the additional attack roll-based cantrip granted by the feat."

        self.instance = Feat(name, prerequisites, benefit, description, usage, normal_use)

        self.load_data("spell_sniper.json")


    def from_dict(self):
        return Feat.from_dict(self.instance_dict)

    def instance_test(self, instance):
        pass
        name = "Spell Sniper"
        prerequisites = "Ability to cast at least one spell"
        benefit = "You have mastered ranged spells and gained the following benefits:\n- When you cast a spell that requires an attack roll, the spell's range is doubled.\n- Your ranged spell attacks ignore half and three-quarters cover.\n- You learn one cantrip that requires an attack roll. Choose the cantrip from any spellcasting class; your spellcasting ability for this cantrip depends on the class you selected."
        description = "The Spell Sniper feat enhances a character's spellcasting abilities and precision. It allows them to extend the range of their ranged spells, ignore cover when making spell attacks, and learn an additional attack roll-based cantrip from any spellcasting class."
        usage = "This feat's benefits apply whenever you cast a spell that requires an attack roll. The extended range and cover-ignoring effects are automatically in effect. To learn a new cantrip, consult the spellcasting rules for the chosen cantrip's spellcasting ability and other relevant details."
        normal_use = "Without the Spell Sniper feat, the character's ranged spells have their regular range and do not gain the benefits of extended range or cover-ignoring effects. The character's cantrip choices would follow the usual rules of their selected spellcasting class, without the additional attack roll-based cantrip granted by the feat."

        self.assertEqual(instance.name, name)
        self.assertEqual(instance.prerequisites, prerequisites)
        self.assertEqual(instance.benefit, benefit)
        self.assertEqual(instance.description, description)
        self.assertEqual(instance.usage, usage)
        self.assertEqual(instance.normal_use, normal_use)


if __name__ == "__main__":
    unittest.main()

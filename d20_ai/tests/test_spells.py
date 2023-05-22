import unittest
from d20_ai.tests.base_test_case import BaseTestCase

from d20_ai.d20_rules.spells import Spell


class TestSpell(unittest.TestCase, BaseTestCase):
    def setUp(self):
        self.instance = Spell(
            "Fireball",
            "Evocation",
            3,
            "1 action",
            "Long (400 feet + 40 feet per caster level)",
            "Instantaneous",
            "Reflex half",
            True,
            ["Verbal", "Somatic"],
            "Conjures a fiery orb that explodes, dealing fire damage to all creatures and objects within a 20-foot radius. Affected creatures can make a Reflex saving throw for half damage.",
        )
        self.load_data("fireball.json")

    def from_dict(self):
        return Spell.from_dict(self.instance_dict)

    def instance_test(self, instance):
        self.assertEqual(instance.name, "Fireball")
        self.assertEqual(instance.school, "Evocation")
        self.assertEqual(instance.level, 3)
        self.assertEqual(instance.casting_time, "1 action")
        self.assertEqual(instance.range, "Long (400 feet + 40 feet per caster level)")
        self.assertEqual(instance.duration, "Instantaneous")
        self.assertEqual(instance.saving_throw, "Reflex half")
        self.assertEqual(instance.spell_resistance, True)
        self.assertListEqual(instance.components, ["Verbal", "Somatic"])
        self.assertEqual(
            instance.description,
            "Conjures a fiery orb that explodes, dealing fire damage to all creatures and objects within a 20-foot radius. Affected creatures can make a Reflex saving throw for half damage.",
        )


if __name__ == "__main__":
    unittest.main()

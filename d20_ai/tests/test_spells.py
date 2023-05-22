import unittest

class TestSpell(unittest.TestCase):
    def test_init(self):
        fireball_spell = Spell("Fireball", "Evocation", 3, "1 action", "Long (400 feet + 40 feet per caster level)", "Instantaneous",
                               "Reflex half", True, ["Verbal", "Somatic"], "Conjures a fiery orb that explodes, dealing fire damage to all creatures and objects within a 20-foot radius. Affected creatures can make a Reflex saving throw for half damage.")

        self.assertEqual(fireball_spell.name, "Fireball")
        self.assertEqual(fireball_spell.school, "Evocation")
        self.assertEqual(fireball_spell.level, 3)
        self.assertEqual(fireball_spell.casting_time, "1 action")
        self.assertEqual(fireball_spell.range, "Long (400 feet + 40 feet per caster level)")
        self.assertEqual(fireball_spell.duration, "Instantaneous")
        self.assertEqual(fireball_spell.saving_throw, "Reflex half")
        self.assertEqual(fireball_spell.spell_resistance, True)
        self.assertListEqual(fireball_spell.components, ["Verbal", "Somatic"])
        self.assertEqual(fireball_spell.description, "Conjures a fiery orb that explodes, dealing fire damage to all creatures and objects within a 20-foot radius. Affected creatures can make a Reflex saving throw for half damage.")

if __name__ == "__main__":
    unittest.main()
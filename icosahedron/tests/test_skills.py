import json
import unittest
from icosahedron.tests.base_test_case import BaseTestCase
from icosahedron.directories import test_data

from icosahedron.d20_rules.skills import Skill


class TestSkill(unittest.TestCase):
    def setUp(self):
        self.skill = {
            "name": "Spellcraft",
            "description": "Spellcraft represents knowledge and understanding of spells, magical items, and the intricacies of spellcasting.",
            "abilityScore": "Intelligence",
            "classSkill": True,
            "synergy": [
                {
                    "skill": "Knowledge (Arcana)",
                    "bonus": 2,
                    "description": "Having ranks in Knowledge (Arcana) provides a +2 synergy bonus to Spellcraft checks.",
                },
                {
                    "skill": "Use Magic Device",
                    "bonus": 2,
                    "description": "Having ranks in Use Magic Device provides a +2 synergy bonus to Spellcraft checks.",
                },
            ],
            "retry": True,
            "special": [
                "Identify Spell: A successful Spellcraft check allows the character to identify a spell as it is being cast or a magic item as it is being used.",
                "Decipher Magical Writings: Spellcraft can be used to understand and interpret magical writings, including scrolls, spellbooks, and magical inscriptions.",
                "Recognize Spells: A character with Spellcraft can identify and recognize spells being cast, allowing them to understand the potential effects and countermeasures.",
                "Determine Magic Item Properties: By examining a magic item, Spellcraft can help determine its properties, functions, and limitations.",
            ],
        }
        with open(test_data("spellcraft.json"), "w") as f:
            json.dump(self.skill, f)

    def test_init(self):
        skill_obj = Skill(
            name="Spellcraft",
            description="Spellcraft represents knowledge and understanding of spells, magical items, and the intricacies of spellcasting.",
            ability_score="Intelligence",
            class_skill=True,
            synergy=[
                {
                    "skill": "Knowledge (Arcana)",
                    "bonus": 2,
                    "description": "Having ranks in Knowledge (Arcana) provides a +2 synergy bonus to Spellcraft checks.",
                },
                {
                    "skill": "Use Magic Device",
                    "bonus": 2,
                    "description": "Having ranks in Use Magic Device provides a +2 synergy bonus to Spellcraft checks.",
                },
            ],
            retry=True,
            special=[
                "Identify Spell: A successful Spellcraft check allows the character to identify a spell as it is being cast or a magic item as it is being used.",
                "Decipher Magical Writings: Spellcraft can be used to understand and interpret magical writings, including scrolls, spellbooks, and magical inscriptions.",
                "Recognize Spells: A character with Spellcraft can identify and recognize spells being cast, allowing them to understand the potential effects and countermeasures.",
                "Determine Magic Item Properties: By examining a magic item, Spellcraft can help determine its properties, functions, and limitations.",
            ],
        )
        self.assertEqual(skill_obj.name, "Spellcraft")
        self.assertEqual(
            skill_obj.description,
            "Spellcraft represents knowledge and understanding of spells, magical items, and the intricacies of spellcasting.",
        )
        self.assertEqual(skill_obj.ability_score, "Intelligence")
        self.assertEqual(skill_obj.class_skill, True)
        self.assertEqual(
            skill_obj.synergy,
            [
                {
                    "skill": "Knowledge (Arcana)",
                    "bonus": 2,
                    "description": "Having ranks in Knowledge (Arcana) provides a +2 synergy bonus to Spellcraft checks.",
                },
                {
                    "skill": "Use Magic Device",
                    "bonus": 2,
                    "description": "Having ranks in Use Magic Device provides a +2 synergy bonus to Spellcraft checks.",
                },
            ],
        )
        self.assertEqual(skill_obj.retry, True)
        self.assertEqual(
            skill_obj.special,
            [
                "Identify Spell: A successful Spellcraft check allows the character to identify a spell as it is being cast or a magic item as it is being used.",
                "Decipher Magical Writings: Spellcraft can be used to understand and interpret magical writings, including scrolls, spellbooks, and magical inscriptions.",
                "Recognize Spells: A character with Spellcraft can identify and recognize spells being cast, allowing them to understand the potential effects and countermeasures.",
                "Determine Magic Item Properties: By examining a magic item, Spellcraft can help determine its properties, functions, and limitations.",
            ],
        )

    def test_to_dict(self):
        skill_obj = Skill.from_dict(self.skill)
        skill_dict = skill_obj.to_dict()
        self.assertEqual(skill_dict, self.skill)

    def test_from_dict(self):
        skill_obj = Skill.from_dict(self.skill)
        self.assertEqual(skill_obj.name, "Spellcraft")
        self.assertEqual(
            skill_obj.description,
            "Spellcraft represents knowledge and understanding of spells, magical items, and the intricacies of spellcasting.",
        )
        self.assertEqual(skill_obj.ability_score, "Intelligence")
        self.assertEqual(skill_obj.class_skill, True)
        self.assertEqual(
            skill_obj.synergy,
            [
                {
                    "skill": "Knowledge (Arcana)",
                    "bonus": 2,
                    "description": "Having ranks in Knowledge (Arcana) provides a +2 synergy bonus to Spellcraft checks.",
                },
                {
                    "skill": "Use Magic Device",
                    "bonus": 2,
                    "description": "Having ranks in Use Magic Device provides a +2 synergy bonus to Spellcraft checks.",
                },
            ],
        )
        self.assertEqual(skill_obj.retry, True)
        self.assertEqual(
            skill_obj.special,
            [
                "Identify Spell: A successful Spellcraft check allows the character to identify a spell as it is being cast or a magic item as it is being used.",
                "Decipher Magical Writings: Spellcraft can be used to understand and interpret magical writings, including scrolls, spellbooks, and magical inscriptions.",
                "Recognize Spells: A character with Spellcraft can identify and recognize spells being cast, allowing them to understand the potential effects and countermeasures.",
                "Determine Magic Item Properties: By examining a magic item, Spellcraft can help determine its properties, functions, and limitations.",
            ],
        )


if __name__ == "__main__":
    unittest.main()

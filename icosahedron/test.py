#!/usr/bin/env python
import unittest

from icosahedron.tests.test_ability_score_roller import TestAbilityScoreRoller
from icosahedron.tests.test_armor_item import TestArmorItem
from icosahedron.tests.test_character import TestCharacter
from icosahedron.tests.test_character_class import TestCharacterClass
from icosahedron.tests.test_character_sheet import TestCharacterSheet
from icosahedron.tests.test_dice_roll import TestDiceRoll
from icosahedron.tests.test_dice_roller import TestDiceRoller
from icosahedron.tests.test_directories import TestDirectories
from icosahedron.tests.test_example import TestExample
from icosahedron.tests.test_feat import TestFeat
from icosahedron.tests.test_generator import TestGenerator
from icosahedron.tests.test_inventory_item import TestInventoryItem
from icosahedron.tests.test_mob_stat_block import TestMobStatBlock
from icosahedron.tests.test_model_context import TestModelContex
from icosahedron.tests.test_package import TestPackage
from icosahedron.tests.test_ring_item import TestMagicRing
from icosahedron.tests.test_skills import TestSkill
from icosahedron.tests.test_spells import TestSpell
from icosahedron.tests.test_weapon_item import TestWeaponItem


class CountSuite(object):
    def __init__(self):
        self.count = 0
        self.s = unittest.TestSuite()

    def add(self, tests):
        self.count += 1
        print("%d: %s" % (self.count, tests.__name__))
        self.s.addTest(unittest.makeSuite(tests))


def suite():
    s = CountSuite()

    s.add(TestAbilityScoreRoller)
    s.add(TestArmorItem)
    s.add(TestCharacter)
    s.add(TestCharacterClass)
    s.add(TestCharacterSheet)
    s.add(TestDiceRoll)
    s.add(TestDiceRoller)
    s.add(TestDirectories)
    s.add(TestExample)
    s.add(TestFeat)
    s.add(TestGenerator)
    s.add(TestInventoryItem)
    s.add(TestMagicRing)
    s.add(TestMobStatBlock)
    s.add(TestModelContex)
    s.add(TestPackage)
    s.add(TestSkill)
    s.add(TestSpell)
    s.add(TestWeaponItem)

    return s.s


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())

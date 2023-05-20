#!/usr/bin/env python
import unittest

from d20_ai.tests.test_ability_score_roller import TestAbilityScoreRoller
from d20_ai.tests.test_dice import TestD20Roll, TestD20Roller
from d20_ai.tests.test_directories import TestDirectories
from d20_ai.tests.test_example import TestExample
from d20_ai.tests.test_inventory_item import (
    TestInventoryItem,
    TestArmorItem,
    TestWeaponItem,
    TestMagicRing,
)
from d20_ai.tests.test_mob_stat_block import TestMobStatBlock
from d20_ai.tests.test_character_sheet import TestD20CharacterSheet
from d20_ai.tests.test_package import TestPackage


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
    s.add(TestD20CharacterSheet)
    s.add(TestD20Roll)
    s.add(TestD20Roller)
    s.add(TestDirectories)
    s.add(TestExample)
    s.add(TestInventoryItem)
    s.add(TestArmorItem)
    s.add(TestWeaponItem)
    s.add(TestMagicRing)
    s.add(TestMobStatBlock)
    s.add(TestPackage)

    return s.s


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())

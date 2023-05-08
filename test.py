#!/usr/bin/env python
import unittest

from d20_ai.tests.test_ability_score_roller import TestAbilityScoreRoller
from d20_ai.tests.test_dice import TestD20Roll, TestD20Roller
from d20_ai.tests.test_directories import TestDirectories
from d20_ai.tests.test_example import TestExample



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
    s.add(TestD20Roll)
    s.add(TestD20Roll)
    s.add(TestDirectories)
    s.add(TestExample)

    return s.s


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())

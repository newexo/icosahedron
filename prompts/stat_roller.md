Prompts to prime the pump, responses not surprising:

    Tell me about the D20 game system.
    Tell me about d20 srd.
    Describe a character class from d20 srd.
    User
    Describe a d20 character sheet.
    For a d20 character, describe how to roll ability scores.
    What are differences between standard, classic and heroic ability score rolling rules.

Here start writing actual code.

    Write a python class for standard ability score rolls.
Response:

    import random
    
    class AbilityScoreRoller:
        def __init__(self):
            self.scores = []
    
        def roll_ability_scores(self):
            for i in range(6):
                dice_rolls = [random.randint(1, 6) for j in range(4)]
                dropped_die = min(dice_rolls)
                score = sum(dice_rolls) - dropped_die
                self.scores.append(score)
            return self.scores

    if __name__ == '__main__':
        roller = AbilityScoreRoller()
        scores = roller.roll_ability_scores()
        print(f"Your ability scores are: {scores}")

Modify.

    Modify AbilityScoreRoller to use a numpy.random.RandomState rather than the random package.

Response:

    import numpy as np
    
    class AbilityScoreRoller:
        def __init__(self, seed=None):
            self.scores = []
            self.rand_state = np.random.RandomState(seed=seed)
    
        def roll_ability_scores(self):
            for i in range(6):
                dice_rolls = self.rand_state.randint(1, 7, size=4)
                dropped_die = np.min(dice_rolls)
                score = np.sum(dice_rolls) - dropped_die
                self.scores.append(score)
            return self.scores
    
    if __name__ == '__main__':
        roller = AbilityScoreRoller(seed=42)
        scores = roller.roll_ability_scores()
        print(f"Your ability scores are: {scores}")

Modify again.

    Create a base class for AbilityScoreRoller with roll_ability_scores abstract and the same __init__ function.

Response:

    from abc import ABC, abstractmethod
    
    class BaseAbilityScoreRoller(ABC):
        def __init__(self, seed=None):
            self.scores = []
            self.seed = seed
    
        @abstractmethod
        def roll_ability_scores(self):
            pass

And

    import numpy as np
    
    class AbilityScoreRoller(BaseAbilityScoreRoller):
        def roll_ability_scores(self):
            rand_state = np.random.RandomState(seed=self.seed)
            for i in range(6):
                dice_rolls = rand_state.randint(1, 7, size=4)
                dropped_die = np.min(dice_rolls)
                score = np.sum(dice_rolls) - dropped_die
                self.scores.append(score)
            return self.scores
    
    if __name__ == '__main__':
        roller = AbilityScoreRoller(seed=42)
        scores = roller.roll_ability_scores()
        print(f"Your ability scores are: {scores}")

Another subclass.

    Implement classic ability score roller with BaseAbilityScoreRoller as base.

Response:

    import numpy as np
    from abc import ABC, abstractmethod
    
    class BaseAbilityScoreRoller(ABC):
        def __init__(self, seed=None):
            self.scores = []
            self.seed = seed
    
        @abstractmethod
        def roll_ability_scores(self):
            pass
    
    class ClassicAbilityScoreRoller(BaseAbilityScoreRoller):
        def roll_ability_scores(self):
            rand_state = np.random.RandomState(seed=self.seed)
            for i in range(6):
                dice_rolls = rand_state.randint(3, 19, size=3)
                score = np.sum(dice_rolls)
                self.scores.append(score)
            return self.scores
    
    if __name__ == '__main__':
        roller = ClassicAbilityScoreRoller(seed=42)
        scores = roller.roll_ability_scores()
        print(f"Your ability scores are: {scores}")

Another subclass.

    Implement heroic ability score roller with BaseAbilityScoreRoller as base.

Response

    import numpy as np
    from abc import ABC, abstractmethod
    
    class BaseAbilityScoreRoller(ABC):
        def __init__(self, seed=None):
            self.scores = []
            self.seed = seed
    
        @abstractmethod
        def roll_ability_scores(self):
            pass
    
    class HeroicAbilityScoreRoller(BaseAbilityScoreRoller):
        def roll_ability_scores(self):
            rand_state = np.random.RandomState(seed=self.seed)
            for i in range(6):
                dice_rolls = rand_state.randint(4, 7, size=3)
                score = np.sum(dice_rolls)
                self.scores.append(score)
            return self.scores
    
    if __name__ == '__main__':
        roller = HeroicAbilityScoreRoller(seed=42)
        scores = roller.roll_ability_scores()
        print(f"Your ability scores are: {scores}")

Here is where it might get interesting.

    Write a unittest testcase to test AbilityScoreRoller.

Response:

    import unittest
    from ability_score_roller import AbilityScoreRoller
    
    class TestAbilityScoreRoller(unittest.TestCase):
        def test_roll_ability_scores(self):
            roller = AbilityScoreRoller()
            scores = roller.roll_ability_scores()
    
            self.assertEqual(len(scores), 6)
            for score in scores:
                self.assertGreaterEqual(score, 3)
                self.assertLessEqual(score, 18)
    
    if __name__ == '__main__':
        unittest.main()

And

    Add a regression test to TestAbilityScoreRoller to verify that ClassicAbilityScoreRoller produces consistent results given seed=42.

Response:
    import unittest
    from ability_score_roller import AbilityScoreRoller, ClassicAbilityScoreRoller
    
    class TestAbilityScoreRoller(unittest.TestCase):
        def test_roll_ability_scores(self):
            # test standard ability score rolling
            roller = AbilityScoreRoller()
            scores = roller.roll_ability_scores()
    
            self.assertEqual(len(scores), 6)
            for score in scores:
                self.assertGreaterEqual(score, 3)
                self.assertLessEqual(score, 18)
    
            # test classic ability score rolling with seed=42
            roller = ClassicAbilityScoreRoller(seed=42)
            scores = roller.roll_ability_scores()
    
            expected_scores = [15, 14, 13, 12, 10, 8]
            self.assertEqual(scores, expected_scores)
    
    if __name__ == '__main__':
        unittest.main()

## Raw results

Raw results are in branch [raw/stat_roller](https://github.com/newexo/d20-ai/tree/raw/stat_roller).

## Steps for fixing

Fixed imports in `test_stat_roller.py`.

Deleted "__main__" code from `stat_roller.py`.

Duplicated standard ability score roller unit test for classic and heroic rollers.

Both classic and heroic rollers were producing values out of the correct range.

# Generate code for ability score roller

## Prompts to prime the pump

    Tell me about the D20 game system.
    Tell me about d20 srd.
    Describe a character class from d20 srd.
    Describe a d20 character sheet.
    For a d20 character, describe how to roll ability scores.
    What are differences between standard, classic and heroic ability score rolling rules.

## Prompts to generate python code

Here start writing actual code.

    Write a python class for standard ability score rolls.
    Modify AbilityScoreRoller to use a numpy.random.RandomState rather than the random package.
    Create a base class for AbilityScoreRoller with roll_ability_scores abstract and the same __init__ function.
    Implement classic ability score roller with BaseAbilityScoreRoller as base.
    Implement heroic ability score roller with BaseAbilityScoreRoller as base.
    Write a unittest testcase to test AbilityScoreRoller.
    Add a regression test to TestAbilityScoreRoller to verify that ClassicAbilityScoreRoller produces consistent results given seed=42.

## Branch for generated raw results

Raw results are in branch [generated/ability_score_roller_first_try](https://github.com/newexo/d20-ai/tree/generated/ability_score_roller_first_try).

## Steps to make code actually work

Recorded steps to make code actually work in commit history of branch [refactor/ability_score_roller_first_try](https://github.com/newexo/d20-ai/tree/refactor/ability_score_roller_first_try).

1. First delete extra code from copy and paste and fix the imports so that tests run. After this, one test runs, but 
does not pass.
2. Generalize test of ranges for ability score rollers. The classic ability score roller gives absurd result of rolling 
48 for one of the ability score.
3. Write regression tests for standard and heroic ability score rollers based on existing classical roller test.
4. Fix classic roller so that scores are within correct ranges.
5. Fix regression tests.

## Final refactor

After the fixes, the code is working, but some naming conventions are inconsistent. Also, the RandomState for the 
rollers is reset at the beginning of each roll, so the scores are the same everytime based on seed.

1. Refactor rename AbilityScoreRoller to StandardAbilityScoreRoller.
2. Add a test which fails for each of the ability score roller tests because results are repeated.

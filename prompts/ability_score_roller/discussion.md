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

# Discussion

## Prompts to prime the pump

- Tell me about the D20 game system.
- What does a player do in D20?
- Explain the steps in character creation.
- Explain step-by-step how to compute hit points, allocate skill points, compute base attack, choose feats and spell slots for a first level human character.
- Explain step-by-step how to compute hit points, allocate skill points, compute base attack, choose feats and spell slots for a character advancing from first level to second level.

## Prompts to generate python code

- Write a python class to compute hit points, base attack bonus, list available feats and determine spell slots for a character either starting at first level or advancing to higher levels.
- Not all classes have spells controlled by intelligence bonus. Cleric spells are based on wisdom and sorcerer spells are based on charisma. Rewrite D20Character to accept a generic spell_ability_modifier rather than intelligence modifier.
- The function determine_spell_slots does not seem to work correctly. Remove it and also remove spell_ability_modifier.
- Remove the race property. It does not seem to have any effect in the code.
- Can base attack bonus be computed directly? It should have a simple formula.
- Is there a similar simple way of calculating available skill points? Add a compute_skill_points method.
- Remove list_available_feats.
- The init method seems to expect character_class to be an instance of some class called CharacterClass. What properties should CharacterClass contain?
- Give CharacterClass functions to translate to and from python dict objects.
- Write a unittest test case to test the init function of CharacterClass.
- Write a unittest test case to test D20Character.
- Give the FighterClass CharacterClass data in JSON format.

## Branch for generated raw results

Raw results are in branch [generate/character_class](https://github.com/newexo/d20-ai/tree/generate/character_class).

## Steps to make code actually work

Recorded steps to make code actually work in commit history of branch [refactor/character_class](https://github.com/newexo/d20-ai/tree/refactor/character_class).

1. Clean up imports and remove unused code. Refactor and rename `D20Character` to `Character`. The test for 
`CharacterClass` passes, but the three tests for `Character` fail because they attempt to initialize `Character` with 
the `intelligence_modifier` parameter.

## Final refactor

1.

## Documentation comments


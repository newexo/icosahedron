# Discussion

## Prompts to prime the pump

- Tell me about the D20 game system.
- How does spell casting work in D20?
- How do spells differ for different classes in D20?
- What are the attributes a player or DM must keep track of for individual spells?
- What are a few typical spells for wizards?
- What are a few typical spells for clerics?
- Describe the Fireball spell.
- Make a table of the fireball spell's attributes that a player would use.
- Make a table for the Protection from Evil spell.


## Prompts to generate python code

- Create a json object with the attributes of the Fireball spell.
- Make a json object for the Protection from Evil spell.
- Write a Python class for Spell consistent with both JSON objects.
- Change the Spell class so that it has functions to translate to and from dict.
- Write a unittest test case to test the init of Spell with the Fireball spell as an example.

## Branch for generated raw results

Raw results are in branch [generate/spells](https://github.com/newexo/d20-ai/tree/generate/spells).

## Steps to make code actually work

Recorded steps to make code actually work in commit history of branch [refactor/spells](https://github.com/newexo/d20-ai/tree/refactor/spells).

1. Fix imports in test_spells.py. The generated test passes.

## Final refactor

1. Made class Spell extend Dictable and TestSpells extend BaseTestCase. Test failed because the generated JSON file used
camel case rather than underscores. Fixing that fixed the error, but two tests still failed.
2. The example JSON object had a field "area". Decided it was simplest to remove that from the JSON for now. All tests 
passed after that change.

## Documentation comments


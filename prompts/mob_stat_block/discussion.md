# Discussion

## Prompts to prime the pump

- Tell me about the D20 game system.
- What is the difference between a player and a DM or GM in D20?
- What kinds of NPCs are there in D20?
- Explain villains and henchmen in D20.
- How does the DM keep track of henchmen, villains, and other NPCs during combat encounters in D20?
- What are the main fields that the DM needs in an NPC stat block to keep track of NPC attributes during combat encounters?
- Create an NPC, a goblin named Iggy, and populate a table representing Iggy's stat block.
- Create a similar table representing the stat block of a minor villain called Bob the Evil Wizard who is Iggy's boss.

## Prompts to generate python code

- Translate the table for Iggy's stat block into a json object.
- Translate Bob the Evil Wizard's stat block into a json object with the same schema as Iggy's.
- Create a python class representing the same stat block data as these json objects. Add functions to read and write as json.
- Write a unit test verifying that the from_json function creates an NPC object correctly from Iggy's json object.
- Write a unittest test case verifying that the from_json function creates an NPC object correctly from Iggy's json object.
- Write a similar test case verifying that from_json works for Bob's json object.

## Branch for generated raw results

Raw results are in branch [generated/mob_stat_block](https://github.com/newexo/d20-ai/tree/generated/mob_stat_block).

## Steps to make code actually work

Recorded steps to make code actually work in commit history of branch [refactor/mob_stat_block](https://github.com/newexo/d20-ai/tree/refactor/mob_stat_block).

1. Remove excess code and fix imports to make code and tests run.
2. Remarkably, this time to test passed without error.

## Final refactor

1. Renamed class from NPC to mob_stat_block.
2. Requested a `to_dict` method and additional tests. The tests passed without error.
3. There is now more than one class with both to and from dict and json methods. These have a common factor and so can
have a common base class. Call this common base class dictable.

## Documentation comments

Fed back class MobStatBlock and requested python comments. Incorporated two of these comments into code.

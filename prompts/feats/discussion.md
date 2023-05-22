# Discussion

## Prompts to prime the pump

- Tell me about the D20 game system.
- Tell me about feats and skills.
- What is a PC?
- Describe a D20 character sheet. What details does it contain and how does the player fill it out?
- Create a character named Alice, a third level neutral good wizard.
- What are Alice's feats?
- Give Alice some feats typical of a level 3 wizard.
- What are the attributes of a feat that a player must know?

## Prompts to generate python code

- Create a json object with these details for the Spell Sniper feat.
- We do not need the "source" field.
- Add a field to describe "normal" use without the feat.
- Create a python class representing Feat. Give functions to translate to and from dict objects.
- Write a unittest test case for Feat which tests the init using Spell Sniper feat as an example.

## Branch for generated raw results

Raw results are in branch [generate/feats](https://github.com/newexo/d20-ai/tree/generate/feats).

## Steps to make code actually work

Recorded steps to make code actually work in commit history of branch [refactor/feats](https://github.com/newexo/d20-ai/tree/refactor/feats).

## Final refactor

The generated code was almost right. The only mistake was that the generated json file had field "normalUse" in camel 
case, while the class expected "normal_use" with underscore.

## Documentation comments


# Discussion

## Prompts to prime the pump

- Tell me about the D20 game system.
- Tell me about feats and skills.
- What is a PC?
- Describe a D20 character sheet. What details does it contain and how does the player fill it out?
- Create a character named Alice, a third level neutral good wizard.
- What are Alice's skills?
- What are the attributes of a skill that a player must know?
- There are two attributes missing in this list of skill attributes. Those are Armor Check Penalty and Retry. Describe these.
- Add one more attribute, Special, for extra information not covered in these attributes.

## Prompts to generate python code

- Create a json object describing the Spellcraft skill.
- What are typical skills for a fighter character?
- Describe the Acrobatics skill.
- Create a json object for Acrobatics following the same schema as the Spellcraft skill.
- Create a python class for the Skill object and give it functions to translate to and from dictionary objects with the same schema as the Spellcraft skill.
- Write a unittest test case for the Skill class. Let the setup method create `self.skill` as a dict object with the Spellcraft skill and use that in unit tests for the `to_dict` and `from_dict` functions of the Skill class.
- Add a test for the `__init__` method of the Skill class.
- Rewrite the `to_dict` test function. It seems incorrect.


## Branch for generated raw results

Raw results are in branch [generate/skills](https://github.com/newexo/d20-ai/tree/generate/skills).

## Steps to make code actually work

This time the code worked almost without modification. The refactoring necessary was to make Skill implement to 
Dictable class to make it easy to translate to and from JSON. There were other classes that also had not been refactored 
to implement Dictable. Did those also in this same refactor. 

Recorded steps to refactor work in commit history of branch [refactor/skills](https://github.com/newexo/d20-ai/tree/refactor/skills).


## Documentation comments

Requested documentation for the Skill class. The comments for the init method and class seemed okay.

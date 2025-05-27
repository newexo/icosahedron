# Discussion

## Prompts to prime the pump

- Tell me about the D20 game system.
- What does a player do in D20?
- What is a PC?
- What tools does a player use to keep track of attributes and inventory of a PC during a D20 game session?
- Describe a D20 character sheet. What details does it contain and how does the player fill it out?
- Create a character named Alice, a third level neutral good wizard.

## Prompts to generate python code

- Encode Alice's character sheet in a json object.
- Encode Alice's character sheet as a python dict.
- Write a python class for a D20 character sheet which has functions to translate to and from a dict.
- Write a unittest test case to test the __init__ method from D20CharacterSheet.
- Write a unittest test case to test the to_dict method.
- Write a unittest test case to test the from_dict method.

## Branch for generated raw results

Raw results are in branch [generate/character-sheet](https://github.com/newexo/icosahedron/tree/generate/character-sheet).

## Steps to make code actually work

Recorded steps to make code actually work in commit history of branch [refactor/character-sheet](https://github.com/newexo/icosahedron/tree/refactor/character-sheet).

The generated code samples were long enough that the full code would have exceeded the length limit for generated text.

1. Delete useless code and fix imports. Two tests fail with KeyError.
2. Fix errors in unit tests.
3. Unit tests passed, but were still incomplete. Added remaining assertions.

## Final refactor

1. Already in good shape, no refactor needed.

## Documentation comments


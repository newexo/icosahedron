# Generate code for ability score roller

## Prompts to prime the pump

    Tell me about the D20 game system.
    Tell me about dice used in D20 system.
    Describe dice rolling mechanics in D20.
    What notation is used to describe dice rolls in D20?

## Prompts to generate python code

    Write a python class to roll dice according to D20 rules.
    Write a json object representing the arguments for D20Roller.roll function.
    Write a function to roll D20Roller given a json object.
    Create a class to encapsulate the json object representing a D20Roller roll.
    Write a unit test for D20Roller.
    Write a unit test for D20Roll.

## Branch for generated raw results

Raw results are in branch [generated/dice_roller](https://github.com/newexo/d20-ai/tree/generated/dice_roller).

## Steps to make code actually work

Recorded steps to make code actually work in commit history of branch [refactor/dice_roller](https://github.com/newexo/d20-ai/tree/refactor/dice_roller).

1. First delete extra code from copy and paste and fix the imports so that tests run. After this, two test runs, but 
does not pass fail because of similar error `missing 1 required positional argument: 'dice_type'`.
2. Request fix for unit tests and a refactor for D20Roll and D20Roller. Managed to improve D20Roll and D20Roller, but 
the tests remained problematic. Eventually decided to accept parts the proposed tests.

## Final refactor

## Documentation comments

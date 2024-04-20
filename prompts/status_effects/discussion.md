# Discussion

## Prompts to prime the pump

- You are a software developer implementing an open source version of the D20 game system. Your task is to produce JSON objects encapsulating game features. Think about your role and say nothing but OK.
- Today you are implementing the combat system. Briefly list what status effects are relevant to the combat system.
- Talk about a couple of these status effect. Give me some details about Paralyzed.
- Tell me about concentration.
- Which of these status effects have limited duration?
- Is death a status effect?
- Is petrification a status effect?
- For the sake of this discussion, consider death to be a status effect. Also consider dying (from HP less than 0) to be a status effect.
- Create a table to describe all status effects listed so far.
- All of these effects so far are negative. What are some positive status effects?
- Add these to the table of status effects.

## Prompts to generate python code

Actually write some code.

- Create a JSON object encapsulating the information from this table.
- Write a Python class encapsulating the status effect object using the pydantic package.
- Write some pytest tests for StatusEffect to prove the class works. Test initialization, loading from dict and saving to dict.


## Branch for generated raw results

Raw results are in branch [generate/status-effects](https://github.com/newexo/icosahedron/tree/generate/status-effects).

## Steps to make code actually work

Recorded steps to make code actually work in commit history of branch []().

1. 

## Final refactor

1.

## Documentation comments


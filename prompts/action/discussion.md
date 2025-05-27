# Discussion

## Prompts to prime the pump

- You are a software developer implementing an open  source version of the D20 game system. Your task is to produce JSON objects encapsulating game features. Think about your role and say nothing but OK.
- Today you are implementing the combat system. Briefly list the features you may need to implement in bullet points.
- Explain initiative order.
- That seems straightforward. What kinds of combat actions and movement actions can a character take in a single round? Under what conditions?
- How many actions per round may a character take?
- Explain attacks of opportunity?
- Explain readied actions.
- Summarize in bullet points, what are the overall types of actions that a character could take in combat. How would they group together?
- That sounds like a good summary. List possible standard actions in bullet points.
- Which of these standard actions cause attacks of opportunity?
- Are there attack actions which might provoke attacks of opportunity?
- List examples of special attacks. Note which might provoke attacks of opportunities.
- List all types of attacks discussed so far.
- What are examples of spell casting and actions similar to spell casting?
- Under what circumstances would using a magic-like ability provoke an attack of opportunity?
- What are examples of move-equivalent actions?
- What are examples of full-round actions?

## Prompts to generate python code

Here start writing actual code.

- Make a table of all actions discussed so far. Have a column for whether action is standard, move or full round action. Have a column for whether the action may provoke attack of opportunity.
- Write this table as a JSON object. For the Action column, use field name "name". For the type column, use field name "action_type". For the May Provoke AoO column, use the field name "aoo". Also add a description field.
- Write a Python class encapsulating the action object using the pydantic package.
- Write some pytest tests for Action to prove the class works. Test initialization, loading from dict and saving to dict.

## Branch for generated raw results

Raw results are in branch [generate/action](https://github.com/newexo/icosahedron/tree/generate/action).

## Steps to make code actually work

Recorded steps to make code actually work in commit history of branch [refactor/action](https://github.com/newexo/icosahedron/tree/refactor/action).

1. Only required fixing import in test_action.py to make tests run.

## Final refactor

1. Already in good shape, no refactor needed.

## Documentation comments


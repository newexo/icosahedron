# Icosahedron

This project records step-by-step building a basic RPG inspired the D20 SRD in python using ChatGPT.

## OGL and SRD

In 2000, Wizards of the Coast published D&D 3.0. This was a very different game system than the AD&D system previously 
published by TSR. The rule system was based on an underlying game system call the D20 System. Like AD&D, this was a turn
based RPG which used polyhedral dice. The rules for the D20 system were based on a simplified game system in which most 
important events were determined by rolling twenty sided dice. Either one die roll would determine outcome when compared
to a fixed number from a chart, or two dice rolls from competing entities would determine the outcome of a contest.

The idea was that simple, and Wizards of the Coast offered the rule system either in commercially published rule books, 
or in a more basic form published online as a System Reference Document (SDR) licensed under the Open Game License 
(OGL). 2000 and 2003, this opened up a world of possibilities for independent game developer to publish compatible rule
system under the OGL. (See Wikipedia: [D20 system](https://en.wikipedia.org/wiki/D20_System) and 
[OGL](https://en.wikipedia.org/wiki/Open_Game_License).)

Games based on these systems were very popular during the years from 2000 to 2021. The Internet was flooded content 
related to the D20 System with detailed discussions of rules, games and personal opinions. As a result there was 
significant data available on the D20 System and the various SRDs in the crawled data used to train large language 
models.

## Enter the LLM

Turn based RPGs are systems based on tabular data. LLMs are very good at transforming between natural language 
explanations and tabular data. Hence, it should be no surprise that models such as GPT contain plausible encoding of 
the D20 System and its variants.

LLMs are also very good at transforming between formats such as tabular data and JSON or other dictionary 
representations in any popular programming language. That is the purpose of this demonstration. This is a test of how 
generative AI can write.

The code itself is incidental. Directory `icosahedron` contains code which was written with the assistance of LLM. Some of that
code worked immediately after generation. Most of it did not and required modification. Each class represents some 
concept from turn-based RPG game rules. None of this code was generated with a direct reference to any actual D20 SDR or
any source other than an LLM and the memory of those developers participating in the project.

What may be more valuable than the code itself the record of the process to produce the code in subdirectories 
[prompts](prompts). These subdirectories each contain a file named transcript.md, which records prompts and responses to 
LLMs, and discussions.md, which explains the prompts used to generate state and what modifications were necessary to 
make the code and unit tests pass.

In this repository there are several branches which preserve parts of this process. Branches named `generate/*` which 
contains raw code from the LLM without attempting to make it work. Those branches named `refactor/*` contain the commits
described in the discussion.md required to make th code work, tests pass and finally added docstring comments.

## Outcome

This repo, icosahedron is not directly an implementation of D20 or any other turn-based RPG. The point of this exercise has 
never been to implement any existing game, but to implement a new game with features which would be similar familiar to 
players of existing games. That icosahedron is not a faithful reproduction of an existing work is a feature in itself. In 
some sense this is a new work rather than a copy of an existing work.

In what sense generated text, code or images represents new work, and in what sense derivative work, I am not in a 
position to say. All I can say is that this work was produced by me and a couple of friends and that we have documented 
the conditions under which we have produced it.

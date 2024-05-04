# Discussion

## Prompts to prime the pump

- Compare python unittest and pytest testing frameworks.

## Prompts to refactor python code

GPT was not intelligent enough to refactor unittest test cases which depended on superclasses directly into pytest test 
cases, but was intelligent enough first to refactor such test cases into classes which did not have a base class. From
there, it was easy to refactor the test cases into pytest test cases.

Refactoring other unittest test cases was simple.

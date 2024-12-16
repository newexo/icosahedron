# Icosahedron Functional Tests

This directory contains functional tests for the Icosahedron library. Functional tests are tests that verify the 
correctness of the library by running it on a set of inputs and comparing the output to the expected output. Often, 
functional tests are expected to run in a test environment that is as close as possible to the production environment.
In the case of the Icosahedron library, this environment may require access to LLM APIs such as OpenAI for GPT-3 and 
Ollama for local language models.

Care should be taken running tests which invoke paid APIs, as this may cost real money.


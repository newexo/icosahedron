from icosahedron.generate.generate_from_example import ModelContext


class MockOpenAI:
    pass


def test_init_model_context_default():
    context = ModelContext(client=MockOpenAI())
    assert 0 == context.temperature
    assert 500 == context.max_tokens
    assert "gpt-4o" == context.model
    assert "####" == context.delimiter


def test_init_model_context():
    context = ModelContext(
        client=MockOpenAI(),
        temperature=0.5,
        max_tokens=100,
        model="fancy-model",
        delimiter="***",
    )
    assert 0.5 == context.temperature
    assert 100 == context.max_tokens
    assert "fancy-model" == context.model
    assert "***" == context.delimiter

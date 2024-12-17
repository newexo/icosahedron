from ...generate.openai_model_context import OpenAIModelContext

from .mocks import MockModelContext


def test_init_model_context_default(context):
    assert 0 == context.temperature
    assert 500 == context.max_tokens
    assert "fancy-model" == context.model_name
    assert "####" == context.delimiter


def test_init_openai_model_context(mock_openai):
    context = OpenAIModelContext(client=mock_openai)
    assert 0 == context.temperature
    assert 500 == context.max_tokens
    assert "gpt-4o-mini" == context.model_name
    assert "####" == context.delimiter


def test_init_model_context():
    context = MockModelContext(
        temperature=0.5,
        max_tokens=100,
        model_name="other-fancy-model",
        delimiter="***",
    )
    assert 0.5 == context.temperature
    assert 100 == context.max_tokens
    assert "other-fancy-model" == context.model_name
    assert "***" == context.delimiter

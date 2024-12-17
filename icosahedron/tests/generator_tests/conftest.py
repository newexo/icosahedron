import pytest
from icosahedron.generate.model_context import ModelContext


class MockOpenAI:
    pass


@pytest.fixture
def mock_openai():
    return MockOpenAI()


@pytest.fixture
def context():
    return ModelContext(model_name="fancy-model")

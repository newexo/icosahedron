import pytest
from icosahedron.generate.model_context import ModelContext


class MockOpenAI:
    pass


@pytest.fixture
def context():
    return ModelContext(client=MockOpenAI())

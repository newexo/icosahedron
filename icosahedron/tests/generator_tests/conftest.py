import pytest
from icosahedron.tests.generator_tests.mocks import MockOpenAI, MockModelContext


@pytest.fixture
def mock_openai():
    return MockOpenAI()


@pytest.fixture
def context():
    return MockModelContext(model_name="fancy-model")

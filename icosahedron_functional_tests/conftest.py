import pytest

from icosahedron.env import load_icosahedron_env

pytest_plugins = ("pytest_asyncio",)


@pytest.fixture
def load_env():
    load_icosahedron_env()

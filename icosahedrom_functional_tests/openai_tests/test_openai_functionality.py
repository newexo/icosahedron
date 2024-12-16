import os

from icosahedron.env import load_icosahedron_env


def test_openai_key_exists():
    load_icosahedron_env()
    assert os.getenv("OPENAI_ORGANIZATION")
    assert os.getenv("OPENAI_API_KEY")

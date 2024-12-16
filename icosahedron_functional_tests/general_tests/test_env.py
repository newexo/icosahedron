import os

from icosahedron.env import find_icosahedron_env, load_icosahedron_env


def test_find_icosahedron_env():
    assert find_icosahedron_env()
    assert os.path.exists(find_icosahedron_env())


def test_load_icosahedron_env():
    load_icosahedron_env()  # just test that this does not throw an error

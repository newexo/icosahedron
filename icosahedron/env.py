from dotenv import load_dotenv, find_dotenv

from .directories import secrets


def find_icosahedron_env():
    return find_dotenv(secrets(".env"))


def load_icosahedron_env():
    _ = load_dotenv(find_icosahedron_env())

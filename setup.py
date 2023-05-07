import sys
from setuptools import setup, find_packages

with open("d20_ai/_version.py") as f:
    version = f.readlines()[-1].split()[-1].strip("\"'")


def forbid_publish():
    argv = sys.argv
    blacklist = ["register", "upload"]

    for command in blacklist:
        if command in argv:
            values = {"command": command}
            print('Command "%(command)s" has been blacklisted, exiting...' % values)
            sys.exit(2)


forbid_publish()

setup(
    name="d20_ai",
    version=version,
    author="Reuben Brasher",
    install_requires=["numpy~=1.24"],
    packages=find_packages(),
    include_package_data=True,
)

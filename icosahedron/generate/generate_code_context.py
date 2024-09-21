from .. import directories


def code_block(code):
    return f"""```python
{code.strip()}
```"""


def file_context(filename, base_dir=directories.code()):
    return f"""## {filename}
From python file `{directories.qualifyname(base_dir, filename)}`"""


def code_context(filename, base_dir=directories.code()):
    with open(directories.qualifyname(base_dir, filename)) as f:
        return f"{file_context(filename, base_dir)}\n\n{code_block(f.read())}"


def untittest_file_context(filename, base_dir=directories.tests()):
    return f"""## {filename}
    From python test file `{directories.qualifyname(base_dir, filename)}`"""


def unittest_code_context(filename, base_dir=directories.tests()):
    with open(directories.qualifyname(base_dir, filename)) as f:
        return f"{file_context(filename, base_dir)}\n\n{code_block(f.read())}"

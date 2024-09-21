import pytest
from ..generate import generate_code_context
from .. import directories


@pytest.fixture
def code_sample():
    with open(directories.test_data("hello.py")) as f:
        return f.read()


def test_code_block(code_sample):
    expected = """```python
print("Hello, world!")
print("Foo bar baz.")
```"""
    assert generate_code_context.code_block(code_sample) == expected


def test_file_context():
    expected = """## hello.py"""
    actual = generate_code_context.file_context("hello.py")
    assert actual.startswith(expected)

    expected = f"From python file `{directories.code('hello.py')}`"
    assert actual.endswith(expected)

    actual = generate_code_context.file_context(
        "hello.py", base_dir=directories.test_data()
    )
    expected = f"From python file `{directories.test_data('hello.py')}`"
    assert actual.endswith(expected)


def test_code_context(code_sample):
    actual = generate_code_context.code_context(
        "hello.py", base_dir=directories.test_data()
    )
    assert actual.startswith(
        generate_code_context.file_context("hello.py", base_dir=directories.test_data())
    )
    assert actual.endswith(generate_code_context.code_block(code_sample))


def test_unittest_file_context():
    expected = """## test_hello.py"""
    actual = generate_code_context.untittest_file_context("test_hello.py")
    assert actual.startswith(expected)

    expected = f"From python test file `{directories.tests('test_hello.py')}`"
    assert actual.endswith(expected)

    actual = generate_code_context.untittest_file_context(
        "test_hello.py", base_dir=directories.test_data()
    )
    expected = f"From python test file `{directories.test_data('test_hello.py')}`"
    assert actual.endswith(expected)


def test_unittest_code_context(code_sample):
    actual = generate_code_context.unittest_code_context(
        "hello.py", base_dir=directories.test_data()
    )
    assert actual.startswith(
        generate_code_context.file_context("hello.py", base_dir=directories.test_data())
    )
    assert actual.endswith(generate_code_context.code_block(code_sample))

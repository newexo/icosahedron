import unittest

from icosahedron.generate.generate_from_example import ModelContext


class MockOpenAI:
    pass


class TestModelContex(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init_model_context_default(self):
        context = ModelContext(client=MockOpenAI())
        self.assertEqual(0, context.temperature)
        self.assertEqual(500, context.max_tokens)
        self.assertTrue(
            "gpt-3.5-turbo" == context.model or "gpt-3.5-turbo-0301" == context.model
        )
        self.assertEqual("####", context.delimiter)

    def test_init_model_context(self):
        context = ModelContext(
            client=MockOpenAI(),
            temperature=0.5,
            max_tokens=100,
            model="fancy-model",
            delimiter="***",
        )
        self.assertEqual(0.5, context.temperature)
        self.assertEqual(100, context.max_tokens)
        self.assertEqual("fancy-model", context.model)
        self.assertEqual("***", context.delimiter)

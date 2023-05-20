import unittest
import d20_ai


class TestPackage(unittest.TestCase):
    def test_something(self):
        self.assertIsNotNone(d20_ai.__version__)  # add assertion here


if __name__ == '__main__':
    unittest.main()

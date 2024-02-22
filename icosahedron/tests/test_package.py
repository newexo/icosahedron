import unittest
import icosahedron


class TestPackage(unittest.TestCase):
    def test_something(self):
        self.assertIsNotNone(icosahedron.__version__)  # add assertion here


if __name__ == "__main__":
    unittest.main()

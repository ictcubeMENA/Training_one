import unittest

from main import greet


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(greet(), "hello world!", "Greet doesn't return hello world!")


if __name__ == '__main__':
    unittest.main()

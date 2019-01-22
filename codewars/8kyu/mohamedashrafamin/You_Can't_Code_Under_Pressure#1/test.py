import unittest
from main import double_integer


class TestSum(unittest.TestCase):

    def test(self):
        self.assertEqual(double_integer(2), 4)


if __name__ == '__main__':
    unittest.main()

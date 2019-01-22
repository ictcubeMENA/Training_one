import unittest
from main import get_age


class TestSum(unittest.TestCase):

    def test(self):
        self.assertEqual(get_age("2 years old"), 2)
        self.assertEqual(get_age("4 years old"), 4)
        self.assertEqual(get_age("5 years old"), 5)
        self.assertEqual(get_age("7 years old"), 7)


if __name__ == '__main__':
    unittest.main()

import unittest

from main import my_parse_int


class Test_my_parse_int(unittest.TestCase):

    def test(self):
        self.assertEqual(my_parse_int("1"), 1)
        self.assertEqual(my_parse_int("  1 "), 1)
        self.assertEqual(my_parse_int("08"), 8)
        self.assertEqual(my_parse_int("5 friends"), "NaN")
        self.assertEqual(my_parse_int("16.5"), "NaN")


if __name__ == '__main__':
    unittest.main()

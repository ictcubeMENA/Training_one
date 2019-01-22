import unittest

from main import remove_exclamation_marks


class TestSum(unittest.TestCase):

    def test(self):
        self.assertEqual(remove_exclamation_marks("Hello World!"), "Hello World")
        self.assertEqual(remove_exclamation_marks("Hello World!!!"), "Hello World")
        self.assertEqual(remove_exclamation_marks("Hi! Hello!"), "Hi Hello")
        self.assertEqual(remove_exclamation_marks(""), "")
        self.assertEqual(remove_exclamation_marks("Oh, no!!!"), "Oh, no")


if __name__ == '__main__':
    unittest.main()

import unittest

from main import remove_duplicate_words


class Test_remove_duplicate_words(unittest.TestCase):

    def test(self):
        self.assertEqual(
            remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"),
            "alpha beta gamma delta")
        self.assertEqual(remove_duplicate_words("my cat is my cat fat"), "my cat is fat")


if __name__ == '__main__':
    unittest.main()

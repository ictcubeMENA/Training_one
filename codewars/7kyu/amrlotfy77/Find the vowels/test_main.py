import unittest

from main import vowel_indices


class Test_vowel_indices(unittest.TestCase):

    def test(self):
        self.assertEqual(vowel_indices("super"), [2, 4])


if __name__ == '__main__':
    unittest.main()

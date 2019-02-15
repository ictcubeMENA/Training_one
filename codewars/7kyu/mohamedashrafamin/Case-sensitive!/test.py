import unittest
from main import case_sensitive


class TestSum(unittest.TestCase):

    def test(self):
        self.assertEqual(case_sensitive('asd'), [True, []])
        self.assertEqual(case_sensitive('cellS'), [False, ['S']])
        self.assertEqual(case_sensitive('z'), [True, []])
        self.assertEqual(case_sensitive(''), [True, []])


if __name__ == '__main__':
    unittest.main()

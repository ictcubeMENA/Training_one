import unittest
from main import solution


class TestSum(unittest.TestCase):

    def test(self):
        self.assertEqual(solution('abcde', 'cde'), True)
        self.assertEqual(solution('abcde', 'abc'), False)


if __name__ == '__main__':
    unittest.main()

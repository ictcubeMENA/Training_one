import unittest

from main import solution


class Test_solution(unittest.TestCase):

    def test(self):
        self.assertEqual(solution('abcde', 'cde'), True)
        self.assertEqual(solution('abcde', 'abc'), False)


if __name__ == '__main__':
    unittest.main()

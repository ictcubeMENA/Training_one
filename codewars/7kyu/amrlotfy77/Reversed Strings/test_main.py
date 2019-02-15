import unittest

from main import solution


class Test_solution(unittest.TestCase):

    def test(self):
        self.assertEqual(solution('world'), 'dlrow')
        self.assertEqual(solution('hello'), 'olleh')
        self.assertEqual(solution(''), '')
        self.assertEqual(solution('h'), 'h')


if __name__ == '__main__':
    unittest.main()

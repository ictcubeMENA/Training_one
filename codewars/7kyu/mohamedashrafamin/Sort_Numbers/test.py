import unittest
from main import solution


class TestSum(unittest.TestCase):

    def test(self):
        self.assertEqual(solution([1, 2, 10, 5]), [1, 2, 5, 10])


if __name__ == '__main__':
    unittest.main()

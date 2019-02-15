import unittest

from main import unique


class Test_unique(unittest.TestCase):

    def test(self):
        self.assertEqual(unique([]), [])
        self.assertEqual(unique([5, 2, 1, 3]), [5, 2, 1, 3])
        self.assertEqual(unique([1, 5, 2, 0, 2, -3, 1, 10]), [1, 5, 2, 0, -3, 10])


if __name__ == '__main__':
    unittest.main()

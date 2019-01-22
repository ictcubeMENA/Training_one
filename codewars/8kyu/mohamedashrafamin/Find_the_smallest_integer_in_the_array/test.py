import unittest

from main import find_smallest_int


class TestSum(unittest.TestCase):

    def test(self):
        self.assertEqual(find_smallest_int([78, 56, 232, 12, 11, 43]), 11)
        self.assertEqual(find_smallest_int([78, 56, -2, 12, 8, -33]), -33)
        self.assertEqual(find_smallest_int([0, 1 - 2 ** 64, 2 ** 64]), 1 - 2 ** 64)


if __name__ == '__main__':
    unittest.main()

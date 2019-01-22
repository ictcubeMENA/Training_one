import unittest
from main import reverse_list


class TestSum(unittest.TestCase):

    def test(self):
        self.assertEqual(reverse_list([1, 2, 3, 4]), [4, 3, 2, 1])
        self.assertEqual(reverse_list([3, 1, 5, 4]), [4, 5, 1, 3])


if __name__ == '__main__':
    unittest.main()

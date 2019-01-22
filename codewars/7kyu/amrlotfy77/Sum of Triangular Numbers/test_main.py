import unittest

from main import sum_triangular_numbers


class Test_sum_triangular_numbers(unittest.TestCase):

    def test(self):
        self.assertEqual(sum_triangular_numbers(6), 56)


if __name__ == '__main__':
    unittest.main()

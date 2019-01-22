import unittest
from main import seats_in_theater


class TestSum(unittest.TestCase):

    def test(self):
        self.assertEqual(seats_in_theater(16, 11, 5, 3), 96)
        self.assertEqual(seats_in_theater(1, 1, 1, 1), 0)
        self.assertEqual(seats_in_theater(13, 6, 8, 3), 18)
        self.assertEqual(seats_in_theater(60, 100, 60, 1), 99)
        self.assertEqual(seats_in_theater(1000, 1000, 1000, 1000), 0)


if __name__ == '__main__':
    unittest.main()

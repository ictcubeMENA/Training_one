import unittest

from main import comb

class Test_comb(unittest.TestCase):





    def test(self):

        self.subTest("Basic tests")

        self.assertEqual(comb([1, 2, 9]), 15)
        self.assertEqual(comb([100]), 0)
        self.assertEqual(comb([1, 2]), 3)
        self.assertEqual(comb([4, 3, 5, 6, 10, 20]), 111)
        self.assertEqual(comb([87, 84, 42, 34, 24, 81, 60, 48, 75]), 1663)
        self.assertEqual(comb(
            [11, 9, 20, 10, 21, 35, 15, 34, 48, 76, 94, 28, 79, 16, 4, 41, 98, 30, 35, 92, 93, 33, 100, 93, 64, 23, 37,
             6, 86, 27, 48, 16, 66, 99, 61, 83, 3, 5, 95]), 9056)


if __name__ == '__main__':
    unittest.main()
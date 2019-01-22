import unittest

from main import dig_pow

class Test_dig_pow(unittest.TestCase):





    def test(self):

        self.subTest("Basic tests")

        self.assertEqual(dig_pow(89, 1), 1)
        self.assertEqual(dig_pow(92, 1), -1)
        self.assertEqual(dig_pow(46288, 3), 51)

if __name__ == '__main__':
    unittest.main()
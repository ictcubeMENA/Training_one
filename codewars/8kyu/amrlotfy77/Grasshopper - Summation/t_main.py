import unittest

from main import summation

class Test_summation(unittest.TestCase):

    def test(self):
        self.assertEqual(summation(1), 1)
        self.assertEqual(summation(8), 36)


if __name__ == '__main__':
    unittest.main()
import unittest
from main import decode


class TestSum(unittest.TestCase):

    def test(self):
        self.assertEqual(decode([20, 12, 18, 30, 21], 1939), "scout")
        self.assertEqual(decode([14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8], 1939), "masterpiece")


if __name__ == '__main__':
    unittest.main()

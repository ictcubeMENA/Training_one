import unittest

from main import encode


class Test_encode(unittest.TestCase):

    def Test_encode(self):
        self.assertEqual(encode("scout", 1939), [20, 12, 18, 30, 21])
        self.assertEqual(encode("masterpiece", 1939), [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8])


if __name__ == '__main__':
    unittest.main()

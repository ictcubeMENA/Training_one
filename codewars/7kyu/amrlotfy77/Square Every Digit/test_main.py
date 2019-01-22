import unittest

from main import square_digits


class Test_square_digits(unittest.TestCase):

    def test(self):
        self.assertEqual(square_digits(9119), 811181)


if __name__ == '__main__':
    unittest.main()

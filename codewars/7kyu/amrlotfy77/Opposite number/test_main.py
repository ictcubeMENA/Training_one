import unittest

from main import opposite


class Test_opposite(unittest.TestCase):

    def test(self):
        self.assertEqual(opposite(1), -1)


if __name__ == '__main__':
    unittest.main()

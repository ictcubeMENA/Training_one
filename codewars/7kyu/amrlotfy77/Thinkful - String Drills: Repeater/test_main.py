import unittest

from main import repeater


class Test_repeater(unittest.TestCase):

    def test(self):
        self.assertEqual(repeater('a', 5), 'aaaaa')
        self.assertEqual(repeater('Na', 16), 'NaNaNaNaNaNaNaNaNaNaNaNaNaNaNaNa')
        self.assertEqual(repeater('Wub ', 6), 'Wub Wub Wub Wub Wub Wub ')


if __name__ == '__main__':
    unittest.main()

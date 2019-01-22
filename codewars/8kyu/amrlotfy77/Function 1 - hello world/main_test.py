import unittest

from main import greet

class Test_greet(unittest.TestCase):

    def test(self):
        self.assertEqual(greet(), "hello world!", "Greet doesn't return hello world!")


if __name__ == '__main__':
    unittest.main()
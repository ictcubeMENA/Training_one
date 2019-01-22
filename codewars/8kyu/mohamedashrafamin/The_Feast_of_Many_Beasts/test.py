import unittest
from main import feast


class TestSum(unittest.TestCase):

    def test(self):
        self.assertEqual(feast("great blue heron", "garlic naan"), True)
        self.assertEqual(feast("chickadee", "chocolate cake"), True)
        self.assertEqual(feast("brown bear", "bear claw"), False)


if __name__ == '__main__':
    unittest.main()

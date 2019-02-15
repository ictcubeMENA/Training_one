import unittest
from main import scale


class TestSum(unittest.TestCase):
    a = "abcd\nefgh\nijkl\nmnop"
    r = "aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp"

    def test(self):
        self.assertEqual(scale(self.a, 2, 3), self.r)
        self.assertEqual(scale("", 5, 5), "")
        self.assertEqual(scale("Kj\nSH", 1, 2), "Kj\nKj\nSH\nSH")


if __name__ == '__main__':
    unittest.main()

import unittest

from main import even_or_odd

class Test_even_or_odd(unittest.TestCase):





    def test(self):
        self.assertEqual(even_or_odd(2) == "Even")
        self.assertEqual(even_or_odd(0) == "Even")
        self.assertEqual(even_or_odd(7) == "Odd")
        self.assertEqual(even_or_odd(1) == "Odd")
        self.assertEqual(even_or_odd(-1) == "Odd")

if __name__ == '__main__':
    unittest.main()
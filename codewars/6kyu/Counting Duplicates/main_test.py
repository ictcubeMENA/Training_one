import main
import unittest

class TestDuplicate(unittest.TestCase):
    def testing(self):
        self.assertEqual(main.duplicate_count("abcde"), 0)
        self.assertEqual(main.duplicate_count("abcdea"), 1)
        self.assertEqual(main.duplicate_count("indivisibility"), 1)

if __name__ == '__main__':
    unittest.main()

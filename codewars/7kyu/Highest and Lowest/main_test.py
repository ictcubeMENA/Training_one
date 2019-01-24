import main
import unittest

class HandLTest(unittest.TestCase):
    def testing(self):
        self.assertEqual(main.high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214")

if __name__ == '__main__':
    unittest.main()

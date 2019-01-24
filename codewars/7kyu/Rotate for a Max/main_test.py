import main
import unittest

class MaxTest(unittest.TestCase):
    def testing(self):
        self.assertEqual(main.max_rot(38458215), 85821534)
        self.assertEqual(main.max_rot(195881031), 988103115)
        self.assertEqual(main.max_rot(896219342), 962193428)
        self.assertEqual(main.max_rot(69418307), 94183076)

if __name__ == '__main__':
    unittest.main()
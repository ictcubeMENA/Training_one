import main
import unittest

class Ticktoward_test(unittest.TestCase):
    def ticktoward_test(self):
        self.assertEqual(main.tick_toward((5,5), (5,7)), [(5,5), (5,6), (5,7)])
        self.assertEqual(main.tick_toward((3,2), (4,5)), [(3,2), (4,3), (4,4), (4,5)])
        self.assertEqual(main.tick_toward((5,1), (5,-2)), [(5,1), (5,0), (5,-1), (5,-2)])

if __name__ == '__main__':
    unittest.main()
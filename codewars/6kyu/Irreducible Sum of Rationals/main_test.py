import main
import unittest

class Fractionstest(unittest.TestCase):
    def fraction_test(self):
        self.assertEqual(main.sum_fracts([[1, 2], [1, 3], [1, 4]]), [13, 12]) 
        self.assertEqual(main.sum_fracts([[1, 3], [5, 3]]), 2)

if __name__ == '__main__':
    unittest.main()
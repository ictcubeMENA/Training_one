import main
import unittest

class OnelineTest(unittest.TestCase):
    def example_test(self):
        a = [1, 2, 3, 4, 5]
        b = [10, 0, 10, 0, 10]
    
        main.fmax(a,b)
        self.assertEqual(a,[10, 2, 10, 4, 10])
if __name__ == '__main__':
    unittest.main()
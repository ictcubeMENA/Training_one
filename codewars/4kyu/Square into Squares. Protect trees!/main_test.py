import main
import unittest

class testsquares(unittest.TestCase):
    def test_squareintosquares(self):
        self.assertEqual(main.decompose(5), [3,4])
        self.assertEqual(main.decompose(8), None)



if __name__ == '__main__':
    unittest.main()
    
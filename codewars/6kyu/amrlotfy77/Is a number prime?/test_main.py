import unittest

from main import is_prime

class Test_is_prime(unittest.TestCase):





    def test(self):

        self.subTest("Basic tests")
        

        self.assertEqual(is_prime(0), False, '0 is not prime')
        self.assertEqual(is_prime(1), False, '1 is not prime')
        self.assertEqual(is_prime(2), True, '2 is prime')

if __name__ == '__main__':
    unittest.main()
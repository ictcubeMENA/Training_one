import unittest

from main import is_uppercase



class Test_is_uppercase(unittest.TestCase):



    def gen_test_case(self):

        self.assertEqual(is_uppercase("c"), False)

if __name__ == '__main__':
    unittest.main()
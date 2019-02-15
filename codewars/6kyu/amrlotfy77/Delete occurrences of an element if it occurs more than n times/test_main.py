import unittest

from main import delete_nth

class Test_delete_nth(unittest.TestCase):





    def test(self):

        self.subTest("Basic tests")

        self.assertEqual(delete_nth([20, 37, 20, 21], 1), [20, 37, 21])
        self.assertEqual(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3), [1, 1, 3, 3, 7, 2, 2, 2])

if __name__ == '__main__':
    unittest.main()
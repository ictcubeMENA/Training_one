import unittest

from main import arrange

class Test_array_diff(unittest.TestCase):





    def test(self):

        self.subTest("Basic tests")
        self.assertEqual(arrange("who hit retaining The That a we taken"), "who RETAINING hit THAT a THE we TAKEN")


if __name__ == '__main__':
    unittest.main()
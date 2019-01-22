import unittest

from main import check,count_smileys

class Test_count_smileys(unittest.TestCase):





    def test(self):

        self.subTest("Basic tests")

        self.assertEqual(count_smileys([]), 0)
        self.assertEqual(count_smileys([':D', ':~)', ';~D', ':)']), 4)
        self.assertEqual(count_smileys([':)', ':(', ':D', ':O', ':;']), 2)
        self.assertEqual(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)

if __name__ == '__main__':
    unittest.main()
import unittest

from main import no_space


class TestSum(unittest.TestCase):

    def test(self):
        self.assertEqual(no_space('8kyu j 8kyu   mBliB8g  imjB8B8  jl  B'), '8kyuj8kyumBliB8gimjB8B8jlB')
        self.assertEqual(no_space('8kyu 8kyu Bi fk8h B 8kyu BB8B B B  B888 c hl8 BhB fd'),
                         '8kyu8kyuBifk8hB8kyuBB8BBBB888chl8BhBfd')
        self.assertEqual(no_space('8aaaaa dddd r     '), '8aaaaaddddr')
        self.assertEqual(no_space('jfBm  gk lf8hg  88lbe8 '), 'jfBmgklf8hg88lbe8')
        self.assertEqual(no_space('8j aam'), '8jaam')


if __name__ == '__main__':
    unittest.main()

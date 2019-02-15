import unittest

from main import reverse_words


class Test_reverse_words(unittest.TestCase):

    def test(self):
        self.assertEqual(reverse_words('The quick brown fox jumps over the lazy dog.'),
                         'ehT kciuq nworb xof spmuj revo eht yzal .god')
        self.assertEqual(reverse_words('apple'), 'elppa')
        self.assertEqual(reverse_words('a b c d'), 'a b c d')
        self.assertEqual(reverse_words('double  spaced  words'), 'elbuod  decaps  sdrow')


if __name__ == '__main__':
    unittest.main()

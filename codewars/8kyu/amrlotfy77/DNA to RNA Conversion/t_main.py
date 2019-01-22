import unittest

from main import DNAtoRNA

class Test_DNAtoRNA(unittest.TestCase):

    def test(self):
        self.assertEqual(DNAtoRNA("TTTT"), "UUUU")
        self.assertEqual(DNAtoRNA("GCAT"), "GCAU")
        self.assertEqual(DNAtoRNA("GACCGCCGCC"), "GACCGCCGCC")

if __name__ == '__main__':
    unittest.main()
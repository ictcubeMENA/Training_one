import unittest
from main import compose


class TestSum(unittest.TestCase):

    def test(self):
        self.assertEqual(compose("byGt\nhTts\nRTFF\nCnnI", "jIRl\nViBu\nrWOb\nNkTB"),
        "bNkTB\nhTrWO\nRTFVi\nCnnIj")
        self.assertEqual(compose("HXxA\nTGBf\nIPhg\nuUMD", "Hcbj\nqteH\nGbMJ\ngYPW"),
        "HgYPW\nTGGbM\nIPhqt\nuUMDH")


if __name__ == '__main__':
    unittest.main()

import main
import unittest

class SquareTest(unittest.TestCase):
    def testing(self):
        self.assertEqual(main.vert_mirror("hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"), "QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw")
        self.assertEqual(main.vert_mirror("IzOTWE\nkkbeCM\nWuzZxM\nvDddJw\njiJyHF\nPVHfSx"), "EWTOzI\nMCebkk\nMxZzuW\nwJddDv\nFHyJij\nxSfHVP")
        self.assertEqual(main.hor_mirror("lVHt\nJVhv\nCSbg\nyeCt"), "yeCt\nCSbg\nJVhv\nlVHt")
        self.assertEqual(main.hor_mirror("njMK\ndbrZ\nLPKo\ncEYz"), "cEYz\nLPKo\ndbrZ\nnjMK")

if __name__ == '__main__':
    unittest.main()

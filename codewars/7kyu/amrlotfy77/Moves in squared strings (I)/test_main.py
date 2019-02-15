import unittest

from main import oper, vert_mirror


class Test_DNAtoRNA(unittest.TestCase):

    def testing(self, actual, expected):
        self.assertEqual(actual, expected)

        self.actual = (oper(vert_mirror, "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"),
                       "QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw")
        self.expected = (oper(vert_mirror, "IzOTWE\nkkbeCM\nWuzZxM\nvDddJw\njiJyHF\nPVHfSx"),
                         "EWTOzI\nMCebkk\nMxZzuW\nwJddDv\nFHyJij\nxSfHVP")


if __name__ == '__main__':
    unittest.main()

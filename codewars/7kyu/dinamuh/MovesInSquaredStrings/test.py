import unittest
from main import vert_mirror
from main import hor_mirror
from main import oper



def test_oper(benchmark):
        assert benchmark(oper,vert_mirror, "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu")== "QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw"
        assert benchmark(oper,vert_mirror, "IzOTWE\nkkbeCM\nWuzZxM\nvDddJw\njiJyHF\nPVHfSx")=="EWTOzI\nMCebkk\nMxZzuW\nwJddDv\nFHyJij\nxSfHVP"
        assert benchmark(oper,hor_mirror, "lVHt\nJVhv\nCSbg\nyeCt")== "yeCt\nCSbg\nJVhv\nlVHt"
        assert benchmark(oper,hor_mirror, "njMK\ndbrZ\nLPKo\ncEYz")== "cEYz\nLPKo\ndbrZ\nnjMK"



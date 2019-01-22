import unittest
from main import compose



def test_compose(benchmark):
        assert benchmark(compose,"byGt\nhTts\nRTFF\nCnnI", "jIRl\nViBu\nrWOb\nNkTB")=="bNkTB\nhTrWO\nRTFVi\nCnnIj"
        assert benchmark(compose,"HXxA\nTGBf\nIPhg\nuUMD", "Hcbj\nqteH\nGbMJ\ngYPW")=="HgYPW\nTGGbM\nIPhqt\nuUMDH"


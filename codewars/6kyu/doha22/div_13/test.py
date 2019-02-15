import unittest
from div_13 import thirt


def test_thirt(benchmark):
    assert benchmark(thirt,8529) == 79
    assert benchmark(thirt,85299258) == 31

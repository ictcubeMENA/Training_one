import unittest
from two_sum import two_sum


def test_two_sum(benchmark):
    assert benchmark(two_sum,[1,2,3], 4) == [0,2]
    assert benchmark(two_sum,[2,2,3], 4) == [0,1]

import unittest
from twisted_sum import compute_sum


def test_compute_sum(benchmark):
    assert benchmark(compute_sum,1) == 1
    assert benchmark(compute_sum,2) == 3

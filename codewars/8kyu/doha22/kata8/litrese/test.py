import unittest
from litrese import litres


def test_litres(benchmark):
    assert benchmark(litres,2) == 1
    assert benchmark(litres,1.4) == 0
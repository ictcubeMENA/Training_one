import unittest
from prim_of_num import num_primorial


def test_num_primorial(benchmark):
    assert benchmark(num_primorial,3) == 30
    assert benchmark(num_primorial,4) == 210

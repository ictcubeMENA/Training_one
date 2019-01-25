import unittest
from playing_digits import dig_pow


def test_dig_pow(benchmark):
    assert benchmark(dig_pow,89,1) == 1
    assert benchmark(dig_pow,92,1) == -1

import unittest
from max_number import max_number


def test_max_number(benchmark):
    assert benchmark(max_number,213) == 321
    assert benchmark(max_number2,7389) == 9873

import unittest
from Div_7  import seven , seven2


def test_get_age(benchmark):
    assert benchmark(seven,1603) == (7,2)
    assert benchmark(seven2,371) == (35,1)

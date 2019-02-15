import unittest
from getting_age import get_age


def test_get_age(benchmark):
    assert benchmark(get_age,"2 years old") == 2
    assert benchmark(get_age,"4 years old") == 4

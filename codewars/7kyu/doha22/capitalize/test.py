import unittest
from capitalize import capitalize, capitalize2


def test_get_age(benchmark):
    assert benchmark(capitalize,"abcdef") == ['AbCdEf', 'aBcDeF']
    assert benchmark(capitalize2,"codewars") == ['CoDeWaRs', 'cOdEwArS']

import unittest
from alarm import set_alarm


def test_set_alarm(benchmark):
    assert benchmark(set_alarm,(True, True)) == False
    assert benchmark(set_alarm,(False, True)) == True
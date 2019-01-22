import unittest
from main import double_integer



def test_double_integer(benchmark):
    assert benchmark(double_integer,2)== 4

import unittest
from main import summation
from main import summation2



def test_summation(benchmark):
    assert benchmark(summation ,1) == 1
    assert benchmark(summation ,8) == 36


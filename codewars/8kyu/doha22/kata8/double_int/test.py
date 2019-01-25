import unittest
from double_int import double_integer

def test_DNAtoRNA(benchmark):
    assert benchmark(double_integer,2) == 4
    assert benchmark(double_integer,3) == 6

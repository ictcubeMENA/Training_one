import unittest
from main import square




def test_square(benchmark):
    assert benchmark(square, 2) == 4
    assert benchmark(square,50)== 2500
    assert benchmark(square ,1)== 1

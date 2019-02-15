import unittest
from jumping_number import jumping_number


def test_jumping_number(benchmark):
    assert benchmark(jumping_number,1) == "Jumping!!"
    assert benchmark(jumping_number, 7) == "Jumping!!"

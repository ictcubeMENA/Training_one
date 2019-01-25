import unittest
from sort_numbers import solution


def test_solution(benchmark):
    assert benchmark(solution,[1,2,10,5]) == [1,2,5,10]
    assert benchmark(solution,[3,1,4]) == [1,3,4]

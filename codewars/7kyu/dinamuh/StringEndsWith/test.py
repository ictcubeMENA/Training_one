import unittest
from main import solution


def test_solution(benchmark):
        assert benchmark(solution,'abcde', 'cde')== True
        assert benchmark(solution,'abcde', 'abc')== False

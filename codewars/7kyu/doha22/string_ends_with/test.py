import unittest
from string_ends_with import solution ,solution2


def test_get_age(benchmark):
    assert benchmark(solution,'abcde', 'cde') == True
    assert benchmark(solution2,'abcde', 'abc') == False

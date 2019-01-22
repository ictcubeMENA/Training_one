import unittest
from main import duplicate_count


def test_duplicate_count(benchmark):
    assert benchmark(duplicate_count,"abcde")== 0
    assert benchmark(duplicate_count,"abcdea")== 1
    assert benchmark(duplicate_count,"indivisibility")== 1





import unittest
from likes import likes


def test_get_age(benchmark):
    assert benchmark(likes,[]) == 'no one likes this'
    assert benchmark(likes,'Peter') == 'Peter likes this'

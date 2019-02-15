import unittest
from remove_duplicates import solve ,solve2


def test_get_age(benchmark):
    assert benchmark(solve,[3,4,4,3,6,3]) == [4,6,3]
    assert benchmark(solve2,[1,2,1,2,1,2,3]) == [1,2,3]

import unittest
from max_rotate import max_rot ,max_rot2


def test_get_age(benchmark):
    assert benchmark(max_rot,38458215) == 85821534
    assert benchmark(max_rot2,195881031) == 988103115

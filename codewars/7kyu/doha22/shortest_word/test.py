import unittest
from shortest_word import find_short


def test_find_short(benchmark):
    assert benchmark(find_short,"bitcoin take over the world maybe who knows perhaps") == 3
    assert benchmark(find_short2,"i want to travel the world writing code one day") == 1

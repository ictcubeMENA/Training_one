import unittest
from main import hero
from main import hero2




def test_hero(benchmark):
    assert benchmark(hero(10, 5), True)
    assert benchmark(hero(7, 4), False)
    assert benchmark(hero(4, 5), False)
    assert benchmark(hero(100, 40), True)
    assert benchmark(hero(1500, 751), False)
    assert benchmark(hero(0, 1), False)


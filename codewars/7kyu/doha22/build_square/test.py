import unittest
from build_square import generateShape


def test_get_age(benchmark):
    assert benchmark(generateShape,3) ==  '+++\n+++\n+++'
    assert benchmark( generateShape, 8) == '++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++'

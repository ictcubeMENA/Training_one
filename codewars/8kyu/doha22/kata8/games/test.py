import unittest
from games import points


def test_points(benchmark):
    assert benchmark(points,['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']) == 30
    assert benchmark(points,['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4']) == 10
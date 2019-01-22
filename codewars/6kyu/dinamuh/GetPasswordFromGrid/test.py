import unittest
from main import get_password
import test

grid = [
    ["x", "l", "m"],
    ["o", "f", "c"],
    ["k", "i", "t"]
  ]
directions = ["rightT", "down", "leftT", "right", "rightT", "down", "left", "leftT"]


def test_get_password(benchmark):
    assert benchmark(get_password,grid,directions)=="lock"

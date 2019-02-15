import unittest
from remove import remove


def test_remove(benchmark):
    assert benchmark(remove,"Hi!",1) == "Hi"
    assert benchmark(remove,"Hi!",100) == "Hi"
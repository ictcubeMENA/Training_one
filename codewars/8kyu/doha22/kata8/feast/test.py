import unittest
from feast import feast


def test_summation(benchmark):
    assert benchmark(feast,"great blue heron", "garlic naan") == True
    assert benchmark(feast,"brown bear", "bear claw") == False
import unittest
from remove_marks import remove_exclamation_marks


def test_remove_exclamation_marks(benchmark):
    assert benchmark(remove_exclamation_marks,"Hello World!") == "Hello World"
    assert benchmark(remove_exclamation_marks,"Hi! Hello!") == "Hi Hello"
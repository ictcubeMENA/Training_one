import unittest
from capitalization import capitalizeWord, capitalizeWord2


def test_get_age(benchmark):
    assert benchmark(capitalizeWord,"word") == "Word"
    assert benchmark(capitalizeWord2,"i") == "I"

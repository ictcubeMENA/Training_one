import unittest
from case_sensitive import case_sensitive, case_sensitive2


def test_get_age(benchmark):
    assert benchmark(case_sensitive,'asd') == [True, []]
    assert benchmark(case_sensitive2,'cellS') == [False, ['S']]

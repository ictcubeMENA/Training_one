import unittest
from main import case_sensitive



def test_case_sensitive(benchmark):
    assert benchmark(case_sensitive,'asd')== [True, []]
    assert benchmark(case_sensitive,'cellS')== [False, ['S']]
    assert benchmark(case_sensitive,'z')== [True, []]
    assert benchmark(case_sensitive,'')== [True, []]

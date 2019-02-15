import unittest
from camal_case import camel_case ,camel_case2


def test_camel_case(benchmark):
    assert benchmark(camel_case,"test case") == "TestCase"
    assert benchmark(camel_case2,"say hello ") == "SayHello"

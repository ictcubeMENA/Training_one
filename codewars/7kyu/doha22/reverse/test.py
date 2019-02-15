import unittest
from reverse import reverse ,reverse2


def test_reverse(benchmark):
    assert benchmark(reverse,["?kn", "ipnr", "utotst", "ra", "tsn", "iksr", "uo", "yer", "ofebta", "eote", "vahu", "oyodpm", "ir", "hsyn", "amwoH"]) ==
    assert benchmark(reverse2,["I", "like", "big", "butts", "and", "I", "cannot", "lie!"]) == ["!", "eilt", "onn", "acIdn", "ast", "t", "ubgibe", "kilI"]

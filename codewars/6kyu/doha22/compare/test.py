import unittest
from compare import comp,comp2

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
aa = [121, 144, 19, 161, 19, 144, 19, 11]
bb = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]

def test_comp(benchmark):
    assert benchmark(comp, a,b) ==  True
    assert benchmark(comp2,aa,bb ) == False

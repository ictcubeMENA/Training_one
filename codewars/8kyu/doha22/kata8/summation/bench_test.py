from main import summation
from main import summation2

def test(benchmark):
    assert benchmark(summation,1) == 1



def test2(benchmark):
    assert benchmark(summation2,8) == 36

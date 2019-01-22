from main import double_integer, doubleInteger


def test1(benchmark):
    assert benchmark(double_integer, 2) == 4


def test(benchmark):
    assert benchmark(doubleInteger, 2) == 4

# py.test
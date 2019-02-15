from main import summation, summation1


def test1(benchmark):
    assert benchmark(summation, 1) == 1


def test(benchmark):
    assert benchmark(summation1, 1) == 1

# py.test

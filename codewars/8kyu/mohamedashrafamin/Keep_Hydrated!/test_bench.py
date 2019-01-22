from main import litres, litres1


def test1(benchmark):
    assert benchmark(litres, 2) == 1


def test(benchmark):
    assert benchmark(litres1, 2) == 1

# py.test

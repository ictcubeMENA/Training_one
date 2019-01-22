from main import opposite


def test1(benchmark):
    assert benchmark(opposite, 1) == -1


def test(benchmark):
    assert benchmark(opposite, 1) == -1

from main import unique, unique1


def test1(benchmark):
    assert benchmark(unique, []) == []


def test(benchmark):
    assert benchmark(unique1, []) == []

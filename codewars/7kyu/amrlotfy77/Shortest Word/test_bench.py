from main import find_short, find_short1


def test1(benchmark):
    assert benchmark(find_short, "bitcoin take over the world maybe who knows perhaps") == 3


def test(benchmark):
    assert benchmark(find_short1, "bitcoin take over the world maybe who knows perhaps") == 3

from main import get_age, get_age1


def test1(benchmark):
    assert benchmark(get_age, "2 years old") == 2


def test(benchmark):
    assert benchmark(get_age1, "2 years old") == 2

# py.test
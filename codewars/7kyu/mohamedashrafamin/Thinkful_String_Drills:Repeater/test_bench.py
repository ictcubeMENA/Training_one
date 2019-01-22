from main import repeater, repeater1


def test1(benchmark):
    assert benchmark(repeater, 'a', 5) == 'aaaaa'


def test(benchmark):
    assert benchmark(repeater, 'a', 5) == 'aaaaa'

# py.test
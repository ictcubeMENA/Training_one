from main import is_opposite, is_opposite1


def test1(benchmark):
    assert benchmark(is_opposite, "ab", "AB") == True


def test(benchmark):
    assert benchmark(is_opposite1, "ab", "AB") == True

# py.test

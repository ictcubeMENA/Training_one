from main import find_smallest_int, findSmallestInt


def test1(benchmark):
    assert benchmark(find_smallest_int, [78, 56, 232, 12, 11, 43]) == 11


def test(benchmark):
    assert benchmark(findSmallestInt, [78, 56, 232, 12, 11, 43]) == 11

# py.test
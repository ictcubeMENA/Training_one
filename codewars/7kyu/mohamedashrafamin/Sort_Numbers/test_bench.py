from main import solution, solution1


def test1(benchmark):
    assert benchmark(solution, [1, 2, 10, 5]) == [1, 2, 5, 10]


def test(benchmark):
    assert benchmark(solution1, [1, 2, 10, 5]) == [1, 2, 5, 10]

# py.test

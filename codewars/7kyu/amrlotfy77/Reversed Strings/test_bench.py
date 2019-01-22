from main import solution1, solution


def test1(benchmark):
    assert benchmark(solution, 'world') == 'dlrow'


def test(benchmark):
    assert benchmark(solution1, 'world') == 'dlrow'

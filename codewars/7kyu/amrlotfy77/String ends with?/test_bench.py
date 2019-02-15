from main import solution, solution1


def test1(benchmark):
    assert benchmark(solution, 'abcde', 'cde') == True


def test(benchmark):
    assert benchmark(solution1, 'abcde', 'cde') == True

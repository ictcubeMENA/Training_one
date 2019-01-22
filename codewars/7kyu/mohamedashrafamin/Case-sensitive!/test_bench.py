from main import case_sensitive, case_sensitive1


def test1(benchmark):
    assert benchmark(case_sensitive, 'asd') == [True, []]


def test(benchmark):
    assert benchmark(case_sensitive1, 'asd') == [True, []]

# py.test
from main import locker_run, locker_run1


def test1(benchmark):
    assert benchmark(locker_run, 1) == [1]


def test(benchmark):
    assert benchmark(locker_run1, 1) == [1]

# py.test
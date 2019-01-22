from main import seats_in_theater, seats_in_theater1


def test1(benchmark):
    assert benchmark(seats_in_theater, 16, 11, 5, 3) == 96


def test(benchmark):
    assert benchmark(seats_in_theater1, 16, 11, 5, 3) == 96

# py.test
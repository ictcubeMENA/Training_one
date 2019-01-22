from main import seats_in_theater


def test_seats_in_theater(benchmark):
    assert benchmark(seats_in_theater, 16, 11, 5, 3) == 96
    assert benchmark(seats_in_theater, 1, 1, 1, 1) == 0
    assert benchmark(seats_in_theater, 13, 6, 8, 3) == 18
    assert benchmark(seats_in_theater, 60, 100, 60, 1) == 99
    assert benchmark(seats_in_theater, 1000, 1000, 1000, 1000) == 0

from main import tick_toward


def test_tick_toward(benchmark):
    assert benchmark(tick_toward, (5, 5), (5, 7)) == [(5, 5), (5, 6), (5, 7)]
    assert benchmark(tick_toward, (3, 2), (4, 5)) == [(3, 2), (4, 3), (4, 4), (4, 5)]
    assert benchmark(tick_toward, (5, 1), (5, -2)) == [(5, 1), (5, 0), (5, -1), (5, -2)]

from main import sum_fracts


def test_sum_fracts(benchmark):
    assert benchmark(sum_fracts, [[1, 2], [1, 3], [1, 4]]) == [13, 12]
    assert benchmark(sum_fracts, [[1, 3], [5, 3]]) == 2

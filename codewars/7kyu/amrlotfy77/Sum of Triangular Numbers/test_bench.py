from main import sum_triangular_numbers, sum_triangular_numbers1


def test1(benchmark):
    assert benchmark(sum_triangular_numbers, 6) == 56


def test(benchmark):
    assert benchmark(sum_triangular_numbers1, 6) == 56

from main import count_positives_sum_negatives,count_positives_sum_negatives1


def test1(benchmark):
      assert benchmark(count_positives_sum_negatives1,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) ==   [10, -65]


def test(benchmark):
    assert benchmark(count_positives_sum_negatives, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) == [10,-65]
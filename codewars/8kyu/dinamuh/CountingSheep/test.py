from main import count_sheeps

array1 = [True, True, True, False,
          True, True, True, True,
          True, False, True, False,
          True, False, False, True,
          True, True, True, True,
          False, False, True, True]


def test_count_sheeps(benchmark):
    assert benchmark(count_sheeps, array1) == 17

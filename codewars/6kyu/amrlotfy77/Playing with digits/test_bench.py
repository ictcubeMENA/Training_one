from main import dig_pow,dig_pow1


def test1(benchmark):
      assert benchmark(dig_pow,89, 1)== 1


def test(benchmark):
    assert benchmark(dig_pow1,89, 1)== 1
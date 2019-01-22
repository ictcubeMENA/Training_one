from main import is_prime,is_prime1


def test1(benchmark):
      assert benchmark(is_prime,0)==False


def test(benchmark):
    assert benchmark(is_prime,0)==False
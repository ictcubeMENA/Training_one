from main import is_uppercase,is_uppercase1


def test1(benchmark):
      assert benchmark(is_uppercase,"c") == False


def test(benchmark):
    assert benchmark(is_uppercase1, "c") == False
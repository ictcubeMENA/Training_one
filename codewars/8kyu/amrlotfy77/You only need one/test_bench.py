from main import check,check1


def test1(benchmark):
      assert benchmark(check,(66, 101), 66) ==  True


def test(benchmark):
    assert benchmark(check1, (66, 101), 66) == True
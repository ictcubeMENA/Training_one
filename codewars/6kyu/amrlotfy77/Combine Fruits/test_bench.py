from main import comb,comb1


def test1(benchmark):
      assert benchmark(comb1,[1, 2, 9])== 15


def test(benchmark):
    assert benchmark(comb1,[1, 2, 9])== 15
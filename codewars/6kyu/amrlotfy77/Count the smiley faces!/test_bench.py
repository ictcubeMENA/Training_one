from main import count_smileys,count_smileys1


def test1(benchmark):
      assert benchmark(count_smileys,[])== 0


def test(benchmark):
    assert benchmark(count_smileys1,[])== 0
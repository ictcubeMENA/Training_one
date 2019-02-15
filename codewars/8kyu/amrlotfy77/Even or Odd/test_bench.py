from main import even_or_odd,even_or_odd1


def test1(benchmark):
      assert benchmark(even_or_odd,2) ==   "Even"


def test(benchmark):
    assert benchmark(even_or_odd1, 2) == "Even"
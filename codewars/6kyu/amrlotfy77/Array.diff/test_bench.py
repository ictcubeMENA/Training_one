from main import delete_nth1,array_diff


def test1(benchmark):
      assert benchmark(array_diff,[1, 2], [1])== [2]


def test(benchmark):
    assert benchmark(array_diff,[1, 2], [1])== [2]
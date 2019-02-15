from main import delete_nth,delete_nth1


def test1(benchmark):
      assert benchmark(delete_nth,[20, 37, 20, 21], 1)==[20, 37, 21]


def test(benchmark):
    assert benchmark(delete_nth1,[20, 37, 20, 21], 1)==[20, 37, 21]
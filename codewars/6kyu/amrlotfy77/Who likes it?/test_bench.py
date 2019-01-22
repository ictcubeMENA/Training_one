from main import likes,likes1


def test1(benchmark):
      assert benchmark(likes,[])=='no one likes this'


def test(benchmark):
    assert benchmark(likes1, []) == 'no one likes this'
from main import remove_char,remove_char1



def test1(benchmark):
      assert benchmark(remove_char,'eloquent') ==  'loquen'


def test(benchmark):
    assert benchmark(remove_char1,'eloquent') ==  'loquen'
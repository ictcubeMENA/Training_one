from main import no_space,no_space1


def test1(benchmark):
      assert benchmark(no_space,'8 j 8   mBliB8g  imjB8B8  jl  B') ==  '8j8mBliB8gimjB8B8jlB'


def test(benchmark):
    assert benchmark(no_space, '8 j 8   mBliB8g  imjB8B8  jl  B') == '8j8mBliB8gimjB8B8jlB'
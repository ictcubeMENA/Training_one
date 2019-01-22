from main import no_space, no_space1


def test1(benchmark):
    assert benchmark(no_space, '8kyu j 8kyu   mBliB8g  imjB8B8  jl  B') == '8kyuj8kyumBliB8gimjB8B8jlB'


def test(benchmark):
    assert benchmark(no_space1, '8kyu j 8kyu   mBliB8g  imjB8B8  jl  B') == '8kyuj8kyumBliB8gimjB8B8jlB'

# py.test

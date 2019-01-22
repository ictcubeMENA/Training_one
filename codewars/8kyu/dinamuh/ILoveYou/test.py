from main import how_much_i_love_you


def test_how_much_i_love_you(benchmark):
    assert benchmark(how_much_i_love_you, 7) == "I love you"
    assert benchmark(how_much_i_love_you, 3) == "a lot"
    assert benchmark(how_much_i_love_you, 6) == "not at all"

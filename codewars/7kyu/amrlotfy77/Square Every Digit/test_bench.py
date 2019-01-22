from main import square_digits, square_digits1


def test1(benchmark):
    assert benchmark(square_digits, 9119) == 811181


def test(benchmark):
    assert benchmark(square_digits1, 9119) == 811181

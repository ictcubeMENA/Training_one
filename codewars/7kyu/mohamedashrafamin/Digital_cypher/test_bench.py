from main import encode, encode


def test1(benchmark):
    assert benchmark(encode, "scout", 1939) == [20, 12, 18, 30, 21]


def test(benchmark):
    assert benchmark(encode, "scout", 1939) == [20, 12, 18, 30, 21]

# py.test
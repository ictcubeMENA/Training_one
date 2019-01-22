from main import decode, decode1


def test1(benchmark):
    assert benchmark(decode, [20, 12, 18, 30, 21], 1939) == "scout"


def test(benchmark):
    assert benchmark(decode1, [20, 12, 18, 30, 21], 1939) == "scout"

# py.test
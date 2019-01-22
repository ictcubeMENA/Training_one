from main import remove, remove1


def test1(benchmark):
    assert benchmark(remove, "Hi!", 1) == "Hi"


def test(benchmark):
    assert benchmark(remove1, "Hi!", 1) == "Hi"

# py.test

from main import greet, greet1


def test1(benchmark):
    assert benchmark(greet) == "hello world!"


def test(benchmark):
    assert benchmark(greet1) == "hello world!"

# py.test

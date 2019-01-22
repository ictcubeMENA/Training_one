from main import capitalize1
from main import capitalize


def test1(benchmark):
    assert benchmark(capitalize1, "abcdef") == ['AbCdEf', 'aBcDeF']


def test(benchmark):
    assert benchmark(capitalize, "abcdef") == ['AbCdEf', 'aBcDeF']

# py.test
from main import capitalize, capitalize1


def test1(benchmark):
    assert benchmark(capitalize, "abcdef") == ['AbCdEf', 'aBcDeF']


def test(benchmark):
    assert benchmark(capitalize1, "abcdef") == ['AbCdEf', 'aBcDeF']

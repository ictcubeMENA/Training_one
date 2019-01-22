from main import remove_every_other, remove_every_other1


def test1(benchmark):
    assert benchmark(remove_every_other, ['Hello', 'Goodbye', 'Hello Again']) ==  ['Hello', 'Hello Again']


def test(benchmark):
    assert benchmark(remove_every_other1, ['Hello', 'Goodbye', 'Hello Again']) ==  ['Hello', 'Hello Again']

# py.test
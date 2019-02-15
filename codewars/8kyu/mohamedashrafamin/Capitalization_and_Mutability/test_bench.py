from main import capitalizeWord, capitalizeWord1


def test1(benchmark):
    assert benchmark(capitalizeWord, 'word') == 'Word'


def test(benchmark):
    assert benchmark(capitalizeWord1, 'word') == 'Word'

# py.test

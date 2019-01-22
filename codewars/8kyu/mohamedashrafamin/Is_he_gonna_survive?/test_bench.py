from main import hero, hero1


def test1(benchmark):
    assert benchmark(hero, 10, 5) == True


def test(benchmark):
    assert benchmark(hero1, 10, 5) == True

# py.test
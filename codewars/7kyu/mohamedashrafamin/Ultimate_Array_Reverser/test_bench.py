from main import reverse, reverse1


def test1(benchmark):
    assert benchmark(reverse, ["I", "like", "big", "butts", "and", "I", "cannot", "lie!"]) == \
           ["!", "eilt", "onn", "acIdn", "ast", "t", "ubgibe", "kilI"]


def test(benchmark):
    assert benchmark(reverse1, ["I", "like", "big", "butts", "and", "I", "cannot", "lie!"]) == \
           ["!", "eilt", "onn", "acIdn", "ast", "t", "ubgibe", "kilI"]

# py.test
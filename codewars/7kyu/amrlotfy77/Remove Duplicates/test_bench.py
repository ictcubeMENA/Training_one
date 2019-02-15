from main import remove_duplicate_words, remove_duplicate_words1


def test1(benchmark):
    assert benchmark(remove_duplicate_words,
                     "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta") == "alpha beta gamma delta"


def test(benchmark):
    assert benchmark(remove_duplicate_words1,
                     "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta") == "alpha beta gamma delta"

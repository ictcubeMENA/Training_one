from main import vowel_indices, vowel_indices1


def test1(benchmark):
    assert benchmark(vowel_indices, "super") == [2, 4]


def test(benchmark):
    assert benchmark(vowel_indices1, "super") == [2, 4]

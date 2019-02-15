from main import get_age


def test_get_age(benchmark):
    assert benchmark(get_age, "2 years old") == 2
    assert benchmark(get_age, "4 years old") == 4
    assert benchmark(get_age, "5 years old") == 5
    assert benchmark(get_age, "7 years old") == 7

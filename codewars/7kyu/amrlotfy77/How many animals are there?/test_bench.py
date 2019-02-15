from main import count_animals, count_animals1


def test1(benchmark):
    assert benchmark(count_animals, "I see 3 zebras, 5 lions and 6 giraffes.") == 14


def test(benchmark):
    assert benchmark(count_animals1, "I see 3 zebras, 5 lions and 6 giraffes.") == 14

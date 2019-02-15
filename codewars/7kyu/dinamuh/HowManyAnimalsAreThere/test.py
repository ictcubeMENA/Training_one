from main import count_animals


def test_count_animals(benchmark):
    assert benchmark(count_animals, "I see 3 zebras, 5 lions and 6 giraffes.") == 14, 'Live from the Savannah'
    assert benchmark(count_animals, "Mom, 3 rhinoceros and 6 snakes come to us!") == 9
    assert benchmark(count_animals, "I do not see any animals here!") == 0

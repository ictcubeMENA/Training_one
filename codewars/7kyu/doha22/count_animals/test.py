import unittest
from count_animals import count_animals,CountAnimals2


def test_get_age(benchmark):
    assert benchmark(count_animals,"I see 3 zebras, 5 lions and 6 giraffes.") == 14
    assert benchmark(CountAnimals2,"I do not see any animals here!") == 0

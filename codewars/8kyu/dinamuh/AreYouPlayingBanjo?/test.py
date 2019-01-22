import unittest
from main import areYouPlayingBanjo


def test_areYouPlayingBanjo(benchmark):
    assert benchmark(areYouPlayingBanjo,"martin") == "martin does not play banjo"
    assert benchmark(areYouPlayingBanjo,"Rikke") == "Rikke plays banjo"
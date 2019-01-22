from main import decompose


def test_areYouPlayingBanjo(benchmark):
    assert benchmark(decompose, 5) == [3, 4]
    assert benchmark(decompose, 8) == None

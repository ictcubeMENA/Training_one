from main import areYouPlayingBanjo,areYouPlayingBanjo1


def test(benchmark):
      assert benchmark(areYouPlayingBanjo,"martin") ==  "martin does not play banjo"


def test1(benchmark):
    assert benchmark(areYouPlayingBanjo1, "martin") == "martin does not play banjo"
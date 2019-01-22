from main import longest_consec,longest_consec1


def test1(benchmark):
      assert benchmark(longest_consec,["zone", "abigail", "theta", "form", "libe", "zas"], 2)=="abigailtheta"


def test(benchmark):
    assert benchmark(longest_consec1, ["zone", "abigail", "theta", "form", "libe", "zas"], 2) == "abigailtheta"
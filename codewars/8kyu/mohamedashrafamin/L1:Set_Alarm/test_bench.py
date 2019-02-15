from main import set_alarm, set_alarm1


def test1(benchmark):
    assert benchmark(set_alarm, True, True) == False


def test(benchmark):
    assert benchmark(set_alarm1, True, True) == False

# py.test

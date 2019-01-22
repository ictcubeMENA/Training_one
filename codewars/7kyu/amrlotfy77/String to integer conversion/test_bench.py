from main import my_parse_int, my_parse_int1


def test1(benchmark):
    assert benchmark(my_parse_int, "1") == 1


def test(benchmark):
    assert benchmark(my_parse_int1, "1") == 1

from repeater import repeater
from repeater import repeater2


def test(benchmark):
    assert benchmark(repeater, 'a' , 5) == 'aaaaa'


def test2(benchmark):
    assert benchmark(repeater2, 'a', 5) == 'aaaaa'

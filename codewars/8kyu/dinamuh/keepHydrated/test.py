from main import litres


def test_litres(benchmark):
    assert benchmark(litres, 2) == 1
    assert benchmark(litres, 1.4) == 0
    assert benchmark(litres, 12.3) == 6
    assert benchmark(litres, 0.82) == 0
    assert benchmark(litres, 11.8) == 5
    assert benchmark(litres, 1787) == 893
    assert benchmark(litres, 0) == 0

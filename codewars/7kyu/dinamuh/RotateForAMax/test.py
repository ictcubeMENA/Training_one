from main import max_rot


def test_max_rot(benchmark):
    assert benchmark(max_rot, 38458215) == 85821534
    assert benchmark(max_rot, 195881031) == 988103115
    assert benchmark(max_rot, 896219342) == 962193428
    assert benchmark(max_rot, 69418307) == 94183076

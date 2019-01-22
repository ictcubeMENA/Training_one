from main import array_diff


def test_array_diff(benchmark):
    assert benchmark(array_diff, [1, 2], [1]) == [2], "a was [1,2], b was [1], expected [2]"
    assert benchmark(array_diff, [1, 2, 2], [1]) == [2, 2], "a was [1,2,2], b was [1], expected [2,2]"
    assert benchmark(array_diff, [1, 2, 2], [2]) == [1], "a was [1,2,2], b was [2], expected [1]"
    assert benchmark(array_diff, [1, 2, 2], []) == [1, 2, 2], "a was [1,2,2], b was [], expected [1,2,2]"
    assert benchmark(array_diff, [], [1, 2]) == [], "a was [], b was [1,2], expected []"

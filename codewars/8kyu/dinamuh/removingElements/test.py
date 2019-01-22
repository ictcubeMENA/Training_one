import unittest
from main import remove_every_other


def test_remove_every_other(benchmark):
    assert benchmark(remove_every_other, ['Hello', 'Goodbye', 'Hello Again']) == ['Hello', 'Hello Again']
    assert benchmark(remove_every_other, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 3, 5, 7, 9]
    assert benchmark(remove_every_other, [[1, 2]]) == [[1, 2]]
    assert benchmark(remove_every_other, [['Goodbye'], {'Great': 'Job'}]) == [['Goodbye']]

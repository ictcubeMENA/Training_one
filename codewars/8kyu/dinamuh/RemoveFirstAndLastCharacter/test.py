import unittest
from main import remove_char



def test_remove_char(benchmark):
        assert benchmark(remove_char,'eloquent')== 'loquen'
        assert benchmark(remove_char,'country')== 'ountr'
        assert benchmark(remove_char,'person')== 'erso'
        assert benchmark(remove_char,'place')== 'lac'
        assert benchmark(remove_char,'ok')== ''

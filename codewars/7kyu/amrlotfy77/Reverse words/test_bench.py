from main import reverse_words, reverse_words1


def test1(benchmark):
    assert benchmark(reverse_words, 'The quick brown fox jumps over the lazy dog.') == \
           'ehT kciuq nworb xof spmuj revo eht yzal .god'


def test(benchmark):
    assert benchmark(reverse_words1, 'The quick brown fox jumps over the lazy dog.') == \
           'ehT kciuq nworb xof spmuj revo eht yzal .god'

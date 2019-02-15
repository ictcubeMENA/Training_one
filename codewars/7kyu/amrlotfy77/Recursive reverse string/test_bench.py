from main import reverse, reverse1


def test1(benchmark):
    assert benchmark(reverse, "hello world") == "dlrow olleh"


def test(benchmark):
    assert benchmark(reverse1, "hello world") == "dlrow olleh"

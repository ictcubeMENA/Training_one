from main import DNAtoRNA
from main import DNAtoRNA1


def test1(benchmark):
    assert benchmark(DNAtoRNA, "TTTT") == "UUUU"


def test(benchmark):
    assert benchmark(DNAtoRNA1, "TTTT") == "UUUU"

# py.test
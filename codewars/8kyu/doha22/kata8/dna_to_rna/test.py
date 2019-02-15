import unittest
from dna_to_rna import DNAtoRNA, DNAtoRNA2


def test_DNAtoRNA(benchmark):
    assert benchmark(DNAtoRNA,"TTTT") == "UUUU"
    assert benchmark(DNAtoRNA2,"GCAT") == "GCAU"

from main import compose, compose1


def test1(benchmark):
    assert benchmark(compose, "byGt\nhTts\nRTFF\nCnnI", "jIRl\nViBu\nrWOb\nNkTB") == "bNkTB\nhTrWO\nRTFVi\nCnnIj"


def test(benchmark):
    assert benchmark(compose1, "byGt\nhTts\nRTFF\nCnnI", "jIRl\nViBu\nrWOb\nNkTB") == "bNkTB\nhTrWO\nRTFVi\nCnnIj"

# py.test
from main import feast, feast1


def test1(benchmark):
    assert benchmark(feast, "great blue heron", "garlic naan") == True


def test(benchmark):
    assert benchmark(feast1, "great blue heron", "garlic naan") == True

# py,test
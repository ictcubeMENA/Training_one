from main import arrange,arrange1


def test1(benchmark):
      assert benchmark(arrange,"who hit retaining The That a we taken")== "who RETAINING hit THAT a THE we TAKEN"


def test(benchmark):
    assert benchmark(arrange, "who hit retaining The That a we taken") == "who RETAINING hit THAT a THE we TAKEN"
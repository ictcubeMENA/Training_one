def count_animals(x):
    d = 0
    z0 = x.split(' ')
    print(z0)

    for w in z0:

        if w.isdigit():
            d += int(w)

    return (d)


def count_animals1(sentence):
    return sum(int(n) for n in sentence.split() if n.isnumeric())

def vowel_indices(w):
    v = ['a', 'e', 'i', 'o', 'u', 'y']
    vt0 = []

    for i, l in enumerate(w):

        if l in v or l in [x.upper() for x in v]:
            vt0.append(i + 1)

    return vt0


def vowel_indices1(word):
    return [i for i, x in enumerate(word, 1) if x.lower() in 'aeiouy']

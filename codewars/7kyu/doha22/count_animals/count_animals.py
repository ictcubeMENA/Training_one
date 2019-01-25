def count_animals(sentence):
    rr =0
    for s in sentence.split(' '):
        if s.isdigit():
            rr +=int(s)
    return rr 

CountAnimals2 = lambda s: sum(int(e) for e in s.split() if e.isdigit())

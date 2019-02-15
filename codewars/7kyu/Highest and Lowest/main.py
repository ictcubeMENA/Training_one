def high_and_low(numbers):
    numbers = list((max(map(int,numbers.split())),min(map(int,numbers.split()))))
    return ' '.join(map(str,numbers))

def high_and_lowB(numbers): 
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
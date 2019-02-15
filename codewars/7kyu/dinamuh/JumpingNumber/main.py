def jumping_number(number):
    x = str(number)
    if len(x) == 1:
        return "Jumping!!"
    c = 0
    for i in x:
        if i.isdigit():
            c += 1

    for i in range(c):
        if i == c - 1:
            break
        z = int(x[i]) - int(x[i + 1])
        k = abs(z)
        if k != 1:
            return "Not!!"

    return "Jumping!!"


def jumping_number2(number):
    arr = list(map(int, str(number)))
    return ('Not!!', 'Jumping!!')[all(map(lambda a, b: abs(a - b) == 1, arr, arr[1:]))]

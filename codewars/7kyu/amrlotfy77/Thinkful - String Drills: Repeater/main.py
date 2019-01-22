def repeater(string, n):
    n = n - 1
    string += string * n
    return string


def repeater1(string, n):
    counter = 0
    new_string = ''
    while (counter < n):
        counter += 1
        new_string = new_string + string
    return new_string

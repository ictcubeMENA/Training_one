def encode(message, key):
    letter_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26
    }
    num_list = []
    key_list = str(key)
    x = 0
    for i in message:
        num_list.append(letter_dict[i] + int(key_list[x]))
        x += 1
        if x >= len(key_list):
            x = 0
    return num_list


def encode1(message, key):
    # initialize variables
    output = []
    i = 0

    # convert key to a list of integers
    key = [int(d) for d in str(key)]

    # encode characters in 'message'
    for char in message:
        n = ord(char) + key[i]
        output.append(n - 96)
        i = (i + 1) % len(key)

    # return the results
    return output

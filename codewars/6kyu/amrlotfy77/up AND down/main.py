def arrange(strng):
    word = strng.split()
    for z in range(len(word) - 1):
        if z % 2:
            if len(word[z]) < len(word[z + 1]):
                word[z], word[z + 1] = word[z + 1], word[z]
        if not z % 2:
            if len(word[z]) > len(word[z + 1]):
                word[z], word[z + 1] = word[z + 1], word[z]

    return ' '.join(z.lower() if not y % 2 else z.upper() for y, z in enumerate(word))

def arrange1(strng):
    words = strng.split()
    for i in range(len(words)):
        words[i:i+2] = sorted(words[i:i+2], key=len, reverse=i%2)
        words[i] = words[i].upper() if i%2 else words[i].lower()
    return ' '.join(words)
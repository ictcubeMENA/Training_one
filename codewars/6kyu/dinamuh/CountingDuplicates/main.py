def duplicate_count(text):
    x = set()
    y = set()
    for char in text:
        char = char.lower()
        if char in x:
            y.add(char)
        x.add(char)
    return len(y)


def duplicate_count2(s):
    return len([c for c in set(s.lower()) if s.lower().count(c) > 1])

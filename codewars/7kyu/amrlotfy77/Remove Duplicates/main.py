def remove_duplicate_words(s):
    words = s.split()
    return (" ".join(sorted(set(words), key=words.index)))


def remove_duplicate_words1(s):
    s = s.split(" ")
    words = []
    for item in s:
        if item not in words:
            words.append(item)
    return " ".join(words)

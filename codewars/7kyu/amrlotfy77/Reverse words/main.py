def reverse_words(str):
    stt = []
    for word in str.split(' '):
        stt.append(word[::-1])
    return ' '.join(stt)


def reverse_words1(str):
    return ' '.join(w[::-1] for w in str.split(' '))

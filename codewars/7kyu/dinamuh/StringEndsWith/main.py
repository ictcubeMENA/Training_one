def solution(string, ending):
    # your code here...
    x = len(ending)
    stri = string[-x:]
    if stri == ending:
        return True
    else:
        return False


def solution2(string, ending):
    return string.endswith(ending)

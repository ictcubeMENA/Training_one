def solution(string, ending):
    end = len(ending)
    end = end * -1
    if (ending == string[end:]):
        return True
    else:
        return False

def solution2(string, ending):
    return string.endswith(ending)

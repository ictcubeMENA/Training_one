def longest_consec(strarr, k):

    n = len(strarr)

    if n == 0 or k > n or k <= 0:
        return ''

    l = 0
    i1 = 0


    for i in range(n - k + 1):

        length = sum([len(s) for s in strarr[i: i + k]])
        print(length)

        if length > l:

            l = length
            i1 = i

    return ''.join(strarr[i1: i1 + k])


def longest_consec1(strarr, k):
    result = ""

    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index + k])
            if len(s) > len(result):
                result = s

    return result



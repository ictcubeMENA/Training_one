def rot_90_clock(strng):
    ar = strng.split('\n')
    return '\n'.join(''.join(j[i] for j in ar)[::-1] for i in range(len(ar[0])))


def diag_1_sym(strng):
    arr = strng.split('\n')
    return '\n'.join(''.join(j[i] for j in arr) for i in range(len(arr[0])))


def selfie_and_diag1(strng):
    ar = strng.split('\n')
    return '\n'.join(ar[i] + '|' + ''.join(p[i] for p in ar) for i in range(len(ar[0])))


def oper(fct, s):
    return fct(s)


def rot_90_clock2(strng):
    return '\n'.join(''.join(x) for x in zip(*strng.split('\n')[::-1]))


def diag_1_sym2(strng):
    return '\n'.join(''.join(x) for x in zip(*strng.split('\n')))


def selfie_and_diag12(strng):
    return '\n'.join('|'.join(x) for x in zip(strng.split('\n'), diag_1_sym(strng).split('\n')))


def oper2(fct, s):
    return fct(s)

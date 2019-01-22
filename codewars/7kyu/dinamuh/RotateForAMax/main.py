def max_rot(n):
    # your code
    arr = []
    arr.append(n)
    x = str(n)
    for i in range(len(x) - 1):
        x = rotate(x, i)
        x = int(x)
        arr.append(x)
    res = arr[0]
    for i in arr:
        if i >= res:
            res = i

    return res


def rotate(a, i):
    a = str(a)
    return a[:i] + a[i + 1:] + a[i]





def max_rot2(n):
    s, arr = str(n), [n]
    for i in range(len(s)):
        s = s[:i] + s[i+1:] + s[i]
        arr.append(int(s))
    return max(arr)
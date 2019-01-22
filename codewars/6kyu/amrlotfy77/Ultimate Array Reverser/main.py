def reverse(a):
    st = ""
    size = []
    res = []
    for i in range(len(a)):
        st += a[i]
        if i >= 1:
            size.append(len(a[i]) + size[i - 1])
        else:
            size.append(len(a[i]))
    for i in range(len(a)):
        if i >= 1:
            tem = st[len(st) - size[i]:len(st) - size[i - 1]]
            res.append(tem[::-1])
        else:
            tem = st[len(st) - size[i]:len(st)]
            res.append(tem[::-1])

    return res
def mix(s1, s2):
    if s1 == s2 or s1 == "" or s2 == "":
        return ""
    s1 = s1.replace(',', '')
    s2 = s2.replace(',', '')
    l1 = []
    s1 = s1.replace(' ', '')
    while len(s1) != 0:
        if s1[0].islower():
            if s1.count(s1[0]) > 1:
                l1.append([s1.count(s1[0]), s1[0], 1, False])
                s1 = s1.replace(s1[0], '')
            else:
                s1 = s1.replace(s1[0], '')
        else:
            s1 = s1.replace(s1[0], '')
    s2 = s2.replace(' ', '')
    while len(s2) != 0:
        if s2[0].islower():
            if s2.count(s2[0]) > 1:
                try:
                    e = l1.index([s2.count(s2[0]), s2[0], 1, False])
                    l1[e][3] = True
                    s2 = s2.replace(s2[0], '')
                except:
                    r = True
                    for i in l1:
                        if i[1] == s2[0]:
                            if s2.count(s2[0]) > i[0]:
                                l1.remove(i)
                                l1.append([s2.count(s2[0]), s2[0], 2, False])
                                s2 = s2.replace(s2[0], '')
                                r = False
                                break
                            else:
                                r = False
                                s2 = s2.replace(s2[0], '')
                                break
                    if r:
                        l1.append([s2.count(s2[0]), s2[0], 2, False])
                        s2 = s2.replace(s2[0], '')
            else:
                s2 = s2.replace(s2[0], '')
        else:
            s2 = s2.replace(s2[0], '')
    res = ""
    out = []
    for i in l1:
        if i[3]:
            res += "=:" + i[1]*i[0]
            out.append(res)
            res = ""
        else:
            res += str(i[2]) + ":" + i[1]*i[0]
            out.append(res)
            res = ""
    return "/".join(sorted(out, key=lambda x: (-len(x), x)))



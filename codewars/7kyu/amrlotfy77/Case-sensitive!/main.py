def case_sensitive(s):
    c = []
    if s.islower() or s == '':
        return [True, c]


    else:
        for x in s:
            if x.isupper():
                c.append(x)

        return [False, c]


def case_sensitive1(s):
    result = [char for char in s if char.isupper()]
    return [result == [], result]

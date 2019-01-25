def case_sensitive(s):
    if (s == s.lower()):
        return [True, []]
    for c in s:
        if (c == c.upper()):
            return [False, [c]]
        


def case_sensitive2(s):
    return [s.islower() or not s, [c for c in s if c.isupper()]]
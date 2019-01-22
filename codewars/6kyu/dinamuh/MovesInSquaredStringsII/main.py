def rot(s):
    return s[::-1]


def selfie_and_rot(s):
    points = '.' * s.index('\n')
    v = s.replace('\n', points + '\n')
    k = s[::-1].replace('\n', '\n' + points)
    return (points + '\n' + points).join((v, k))


def oper(fct, s):
    return fct(s)






def rot2(string):
    return string[::-1]

def selfie_and_rot2(string):
    s_dot = '\n'.join([ s+'.'*len(s) for s in string.split('\n') ])
    return s_dot+'\n'+rot(s_dot)

def oper2(fct, s):
    return fct(s)
def vert_mirror(strng):
    s = []
    i = 0
    while i < len(strng.split('\n')):
        s.append(strng.split('\n')[i][::-1] )
        i += 1
    return '\n'.join(s)
def hor_mirror(strng):
    s = strng.split('\n')[::-1]
    return '\n'.join(s)
def oper(fct, s):
    # your code
    return fct(s)

def vert_mirrorB(s):
    return "\n".join(line[::-1] for line in s.split("\n"))

def hor_mirrorB(s):
    return "\n".join(s.split("\n")[::-1])

def operB(fct, s):
    return fct(s)
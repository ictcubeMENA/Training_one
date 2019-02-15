def no_space(x):

    l = []
    for i in x:
        if i == " " :
            
            continue
        l.append(i)
    return ''.join(l)

def no_space1(x):
    x = x.replace(" ", "")
    return x
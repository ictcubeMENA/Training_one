def remove_exclamation_marks(s):
    l = []
    for i in s:
        if i == "!" :
            
            continue
        l.append(i)
    return ''.join(l)

def remove_exclamation_marks1(s):
    x = s.replace("!","")
    return x
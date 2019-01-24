def mirror(text):
    maxi = max([len(i)for i in text.split(' ')])
    lst = [' '*(maxi-len(i))+i for i in text.split(' ')]    
    return '*' *(maxi + 4) + '\n* ' +' *\n* '.join([i[::-1] for i in lst]) + ' *\n' + '*' *(maxi + 4)

def mirrorB(s):
    lst = s.split()
    x   = max(map(len,lst))
    border = '*'*(x+4)
    return '\n'.join((border, '\n'.join(f'* {w.rjust(x)[::-1]} *' for w in lst) ,border))
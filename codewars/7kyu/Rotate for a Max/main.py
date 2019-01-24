def max_rot(n):
    i = 0
    list = [str(n)]
    
    while i < len(str(n)):
        n1 = list[i] + list[i][i]
        n1 = n1[:i] + n1[i+1:]
        list.append(n1)
        i += 1
    list = map(int,list)    
    return max(list)

def max_rotB(n):
    s, arr = str(n), [n]
    for i in range(len(s)):
        s = s[:i] + s[i+1:] + s[i]
        arr.append(int(s))
    return max(arr)
def max_rot(n):
    s= str(n)
    array= [n]
    for i in range(len(s)):
        s=s[:i] + s[i+1:] +s[i] 
        x = int(s)
        array.append(x)
    return max(array)
        
def max_rot2(n):
    maximum = n
    s = list(str(n))
    for i in range(len(s) - 1):
        s.append(s.pop(i))
        current = int(''.join(s))
        if current > maximum:
            maximum = current
    return maximum

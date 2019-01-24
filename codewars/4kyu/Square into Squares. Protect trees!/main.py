def decompose(n):
    r = 0
    res = [n]
    while res:
        c = res.pop()
        r += c*c
        for j in range(c-1,0,-1):
            if r - j*j >= 0:
                r = r-j*j
                res.append(j)
                if r == 0:
                    res.sort()
                    return res
          
    return None 

def decomposeB(n):
    total = 0
    answer = [n]
    while len(answer):
        temp = answer.pop()
        total += temp ** 2
        for i in range(temp - 1, 0, -1):
            if total - (i ** 2) >= 0:
                total -= i ** 2
                answer.append(i)
                if total == 0:
                    return sorted(answer)
    return None

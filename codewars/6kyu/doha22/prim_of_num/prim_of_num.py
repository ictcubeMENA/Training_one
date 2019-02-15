def num_prime(x):
    if (x==2):
        return(True)
    else:
        for i in range(2, x): 
            if (x % i) == 0:   
                break
        else: 
            return True
    
def num_primorial(n):
    res = 2 # start of prime numbers
    pr = 1
    c = 0
    for i in range(2,100000000):
        if (num_prime(res)==True):
            pr *=i
            res += 1
            c +=1
            if c== n :
                break
    
        else:
            res +=1
    return pr       
                
def num_prime2(n):
    primorial, x, n = 2, 3, n-1
    while n:
        if all(x % d for d in range(3, int(x ** .5) + 1, 2)):
            primorial *= x
            n -= 1
        x += 2
    return primorial

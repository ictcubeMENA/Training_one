def summation(num):
    #pass # Code here
    total = 0
    for i in range(0,num+1):
        total += i
    return total
    
def summation2(num):
    return sum(xrange(num + 1))
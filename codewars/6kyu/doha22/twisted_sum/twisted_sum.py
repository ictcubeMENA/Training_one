def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def compute_sum(n):
    sum_num = 0
    for i in range(0 , n+1):
        sum_num += sum_digits(i)
    return sum_num 

def compute_sum2(n):
    return sum(int(c) for i in range(1, n+1) for c in str(i))
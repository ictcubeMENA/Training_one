def summation(n):
    n = int(n)

    sum = 0
    for num in range(0, n + 1, 1):
        sum = sum + num
    return sum


def summation1(num):
    return (1+num) * num / 2

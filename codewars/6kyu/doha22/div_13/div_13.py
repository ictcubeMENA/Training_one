def thirt(n):
    p = [1, 10, 9, 12, 3, 4]
    sum = 0

    while 1:
        total = 0
        for index, digit in enumerate(str(n)[::-1]):
            current_index = index % len(p)
            total += int(digit) * p[current_index]

        if sum == total:
            return sum

        sum = total
        n = total



array = [1, 10, 9, 12, 3, 4]

def thirt2(n):
    total = sum([int(c) * array[i % 6] for i, c in enumerate(reversed(str(n)))])
    if n == total:
        return total
    return thirt(total)

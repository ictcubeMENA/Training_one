def decompose(n):
    m = n ** 2
    arr = []
    while m:
        for i in range(1, n, 1):
            mul = (n - i) * (n - i)
            if m >= mul:
                m = m - mul
                arr.append(n - i)
            if m == 0:
                arr.sort()
                return arr
    return None


def decompose2(n):
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

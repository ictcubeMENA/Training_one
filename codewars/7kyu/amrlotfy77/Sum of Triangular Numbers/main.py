def sum_triangular_numbers(n):
    if n < 0:
        return 0

    sum = sum_triangular_numbers(n - 1)

    x = sum + (n * (n + 1)) / 2
    return x


def sum_triangular_numbers1(n):
    return n * (n + 1) * (n + 2) / 6 if n > 0 else 0

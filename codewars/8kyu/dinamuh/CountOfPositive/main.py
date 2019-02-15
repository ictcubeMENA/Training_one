def count_positives_sum_negatives(arr):
    # your code here
    countp = 0
    sumn = 0
    if len(arr) == 0:
        return []
    for i in arr:
        if i > 0:
            countp += 1
        else:
            sumn += i
    return [countp, sumn]


def count_positives_sum_negatives2(arr):
    if not arr: return []
    pos = 0
    neg = 0
    for x in arr:
        if x > 0:
            pos += 1
        if x < 0:
            neg += x
    return [pos, neg]

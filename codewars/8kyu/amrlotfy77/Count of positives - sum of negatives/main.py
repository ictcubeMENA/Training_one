def count_positives_sum_negatives(arr):
    if not arr:
        return []
    pos = 0
    neg = 0
    for n in arr:
        if n > 0:
            pos = pos + 1
        else:
            neg = neg + n
    return [pos, neg]


def count_positives_sum_negatives1(arr):
    if not arr: return []
    pos = 0
    neg = 0
    for x in arr:
      if x > 0:
          pos += 1
      if x < 0:
          neg += x
    return [pos, neg]
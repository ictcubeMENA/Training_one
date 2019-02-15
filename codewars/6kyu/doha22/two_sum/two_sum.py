from collections import defaultdict

def two_sum(numbers, target):

    lookup = defaultdict(list)
    for i, num in enumerate(numbers):
        needed = target - num
        if needed in lookup:
            return [lookup[needed][0], i]
        lookup[num].append(i)

    return None

def two_sum2(nums, t):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]
def solve(arr):
    for x in range(max(arr)+1):
        while arr.count(x)>1:
            arr.remove(x)
    return arr

def solve2(arr):
    return list(dict.fromkeys(arr[::-1]))[::-1]

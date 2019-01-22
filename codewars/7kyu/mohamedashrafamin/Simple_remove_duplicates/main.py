def solve(arr):
    for i in range(len(arr)):
        try:
            if arr.index(arr[i], i+1, len(arr)):
                arr[i] = -20
                continue
        except:
            continue
    res = []
    for i in range(len(arr)):
        if arr[i] != -20:
            res.append(arr[i])

    return res


print(solve([3,4,4,3,6,3]))
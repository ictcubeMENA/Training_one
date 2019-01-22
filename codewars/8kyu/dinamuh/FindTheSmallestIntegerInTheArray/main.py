def find_smallest_int(arr):
    x = arr[0]
    for i in arr:
        if i < x:    x = i
    return x



def findSmallestInt(arr):
    return min(arr)
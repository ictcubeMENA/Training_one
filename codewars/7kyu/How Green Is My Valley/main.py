def make_valley(arr):
    arr1 = []
    arr2 = []
    i = 0
    n = 1
    arr.sort(reverse = True)
    while i < len(arr):
        arr1.append(arr[i])
        i += 2
        
    while n < len(arr):
        arr2.append(arr[n])
        n += 2 
    arr2.sort() 
    arr1.extend(arr2)
    return arr1

def make_valleyB(arr):
    arr = sorted(arr, reverse = True)
    return arr[::2] + arr[1::2][::-1]
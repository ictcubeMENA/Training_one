def make_valley(arr):
    # your code
    arr.sort()
    arr.reverse()
    l=[]
    r=[]
    x=len(arr)
    arr1=[]
    for i in range(x):
        if i%2==0:
            l.append(arr[i])
        elif i%2==1:
            r.append(arr[i])
    r.reverse()
    arr1=l+r
    return arr1



def make_valley2(arr):
    arr = sorted(arr, reverse = True)
    return arr[::2] + arr[1::2][::-1]
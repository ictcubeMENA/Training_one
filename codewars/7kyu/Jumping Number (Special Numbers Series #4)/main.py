def jumping_number(number):
    snum = str(number)
    if len(snum) == 1:
        return 'Jumping!!'
    diff = []
    for i in range(1,len(snum)):
        diff.append(abs(int(snum[i-1]) - int(snum[i])))
    if set(diff) != {1}:
        return 'Not!!'
    else:
        return 'Jumping!!'
        
def jumping_numberB(number):
    arr = list(map(int, str(number)))
    return ('Not!!', 'Jumping!!')[all(map(lambda a, b: abs(a - b) == 1, arr, arr[1:]))]
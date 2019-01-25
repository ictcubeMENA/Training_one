def jumping_number(number):
    print(number)
    i=0
    x=[int(i) for i in str(number)]
    if(len(x) == 1):
            return 'Jumping!!'
    for i in range(len(x)-1):
        
        if x[i+1] - x[i] != 1 and x[i] - x[i+1]!= 1: 
            return 'Not!!'
    return 'Jumping!!'

def jumping_number2(number):
    arr = list(map(int, str(number)))
    return ('Not!!', 'Jumping!!')[all(map(lambda a, b: abs(a - b) == 1, arr, arr[1:]))]

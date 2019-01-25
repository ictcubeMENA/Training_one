def points(games):

    count = 0
    for sc in games:
        scores = sc.split(':')
        x=int(scores[0])
        y=int(scores[1])
    
    
        if (x>y):
             count += 3
        elif(x==y):
            count += 1
        else:
            0
    return count
    
def points2(games):
    return sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in games))
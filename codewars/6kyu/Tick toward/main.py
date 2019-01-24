def tick_toward(start, target):
    lst = [start]
    n = max(abs(target[0]-start[0]),abs(target[1]-start[1]))
    i = 0
    while i < n:
        if lst[i][0] < target[0]:
            num0 = lst[i][0]+1
        elif lst[i][0] > target[0]:
            num0 = lst[i][0]-1    
        else:
            num0 = lst[i][0]
            
        if lst[i][1] < target[1]:
            num_1 = lst[i][1]+1
        elif lst[i][1] > target[1]:
            num_1 = lst[i][1]-1    
        else:
            num_1 = lst[i][1]
        lst.append((num0,num_1)) 
        i += 1
    return lst

def tick_towardB(start, target):
    x1, y1 = target
    points = [start]
    while points[-1] != target:
        x2, y2 = points[-1]
        a, b = (x2 < x1) - (x2 > x1), (y2 < y1) - (y2 > y1)
        points.append((x2 + a, y2 + b))
    return points    
def tick_toward(start, target):
    lst = [start]
    v = abs(target[0] - start[0])
    w = abs(target[1] - start[1])
    number = max(v, w)
    i = 0
    while i < number:
        if lst[i][0] < target[0]:
            x = lst[i][0] + 1
        elif lst[i][0] > target[0]:
            x = lst[i][0] - 1
        else:
            x = lst[i][0]

        if lst[i][1] < target[1]:
            y = lst[i][1] + 1
        elif lst[i][1] > target[1]:
            y = lst[i][1] - 1
        else:
            y = lst[i][1]
        lst.append((x, y))
        i += 1
    return lst


def tick_toward2(start, target):
    x1, y1 = target
    points = [start]
    while points[-1] != target:
        x2, y2 = points[-1]
        a, b = (x2 < x1) - (x2 > x1), (y2 < y1) - (y2 > y1)
        points.append((x2 + a, y2 + b))
    return points

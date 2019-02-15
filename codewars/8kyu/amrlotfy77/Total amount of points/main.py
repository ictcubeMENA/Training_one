def points(games):
    sum = 0
    for x in games:

        if x[0] > x[2]:

         sum = sum + 3

        if x[0] < x[2]:
            sum = sum + 0

        if x[0] == x[2]:
            sum = sum + 1


    return sum




def points1(games):
    count = 0
    for score in games:
        res = score.split(':')
        if res[0]>res[1]:
            count += 3
        elif res[0] == res[1]:
            count += 1
    return count
def points(games):
    games
    count = 0
    for i in games:
        x = i.split(":")
        if int(x[0]) > int(x[1]):
            count += 3
        elif int(x[0]) == int(x[1]):
            count += 1
    return count


def points2(games):
    count = 0
    for score in games:
        res = score.split(':')
        if res[0] > res[1]:
            count += 3
        elif res[0] == res[1]:
            count += 1
    return count

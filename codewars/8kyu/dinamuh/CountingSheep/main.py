def count_sheeps(arrayOfSheeps):
    count = 0
    for i in arrayOfSheeps:
        if i == True:
            count += 1
    return count


def count_sheeps2(arrayOfSheeps):
    return arrayOfSheeps.count(True)

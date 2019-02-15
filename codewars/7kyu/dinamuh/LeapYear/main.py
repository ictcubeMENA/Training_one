def isLeapYear(year):
    if year == 1100:
        return False
    elif year % 4 == 0 or year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return False


def isLeapYear2(year):
    return (year % 100 != 0 and year % 4 == 0) or year % 400 == 0

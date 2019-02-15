def feast(beast, dish):

    x = len(beast)
    y = len(dish)

    if beast[0] == dish[0]:

        if beast[x-1] == dish[y-1]:



         return  True
        else: 
            return False

    else:
        return False


def feast1(beast, dish):
    return beast[0]==dish[0] and dish[-1]==beast[-1]
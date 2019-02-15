def feast(beast, dish):
    # your code here
    pass
    if((dish[0]==beast[0])& (dish[-1]==beast[-1])): 
        return True
    else:
        return False

def feast2(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]
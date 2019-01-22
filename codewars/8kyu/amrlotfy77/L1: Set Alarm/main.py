def set_alarm(employed, vacation):


    if employed == True and vacation == True :

        return False

    if employed == False and vacation == True :

        return False

    if employed == False and vacation == False:
        
        return False

    if employed == True and vacation == False:
        return True


def set_alarm1(employed, vacation):
    # Your code here
    if employed:
        if vacation:
            return False
        return True
    return False
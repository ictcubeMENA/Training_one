def areYouPlayingBanjo(name):

   if name[0] == "R" or name[0] == "r":

       c = name + " plays banjo"

       return c
   else :

       c = name + " does not play banjo"

       return c



def areYouPlayingBanjo1(name):
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'

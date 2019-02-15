def areYouPlayingBanjo(name):
    # Implement me!
    if (name.startswith("R") |name.startswith("r") ):
        return name + " "+"plays banjo"
    else:
        return name +" "+ "does not play banjo"
   # return name

def areYouPlayingBanjo2(name):
    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo";
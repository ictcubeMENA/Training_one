def areYouPlayingBanjo(name):
    if name[0] == "r" or name[0] == "R":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


def areYouPlayingBanjo2(name):
    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo";

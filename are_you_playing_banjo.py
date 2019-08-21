def areYouPlayingBanjo(name):
    x = list(name)
    if x[0] == "R" or x[0] == "r":
        return(name + " plays banjo")
    else:
        return(name + " does not play banjo")
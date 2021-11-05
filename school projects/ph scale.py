#task 1: pH scale
def chemical_strength(pH):

    # if the pH is less than 7, it is an acidic chemical
    if pH >= 0 and pH < 7:
        if pH >= 0 and pH <= 1:
            return('very strong acid')
        elif pH > 1 and pH < 4:
            return('strong acid')
        elif pH == 4:
            return('plain acid')
        elif pH > 4 and pH < 6:
            return('weak acid')
        elif pH >= 6 and pH < 7:
            return('very weak acid')

    # if the pH is more than 7, it is a basic chemical
    elif pH >7 and pH <= 14:
        if pH > 7 and pH <= 8:
            return('very weak base')
        elif pH > 8 and pH < 10:
            return('weak base')
        elif pH == 10:
            return('plain base')
        elif pH > 10 and pH < 13:
            return('strong base')
        elif pH >= 13 and pH <= 14:
            return('very strong base')

    # if the pH is exactly 7, the chemical is neutral
    elif pH == 7:
        return('neutral')

    else:
       return('bad measurement')



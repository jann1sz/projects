#task 2: light switches
def light_status(s1, s2):

    light_minmax = [50, 100]
    if 100 >= s1 >= 50 and 100 >= s2 >= 50:
        return('on')

    elif s1 + s2 == max(light_minmax):
        return('on')


    elif s1 - s2 == min(light_minmax) or s2 - s1 == min(light_minmax):
        if s1 > 100 or s2 > 100:
            return('invalid switch')
        else:
            return('on')


    elif s1 > 100 or s2 > 100:
        return('invalid switch')


    elif s1 < 1 or s2 < 1:
        return('invalid switch')

    else:
        return('off')
      
      
      

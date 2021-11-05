#function that tells us the max of parameters a,b, and c. the parameters
#b and c are not required inputs.

def max_few(a, b=None, c=None):

    #if only the value of a is given, return a
    if b == None and c == None:
        return a
    
    #elif the values of a and b are given, return the larger value (a or  b)
    elif c == None:
        if a > b:
            return a
        elif b > a:
            return b

    #else if the values of a, b, and c are give, return the larger value of the
    #three given
    else:
        if a > b and a > c:
            return a
        elif b > a and b > c:
            return b
        elif c > a and c > b:
            return c
    
max_few(100,500)

def extract_min(xs):
    
    #indexmark list holds the index where the minimum is (minimum at the left
    #furthest side in the case there are duplicates)
    indexmark = []
    i = 0
    
    #minimum is automatically assigned the first number in the list xs
    min = xs[i]
    
    #index of the minimum starts at zero since the first number of the list has
    #an index of zero
    indexmark.append(0)
    
    #loop that finds the minimum of the list xs
    for i in range(len(xs)):
        value = xs[i]
        if min > value:
            min = xs[i]
            
            #take out the index in indexmark and replace it with the new index
            #where the current minimum is
            indexmark.pop(0)
            indexmark.append(i)
    
    #loop that takes out the minimum at the stored index in indexmark
    for j in range(len(xs)):
        if j in indexmark:
            value = indexmark[0]
            xs.pop(value)
    
    return min
    

extract_min([9,9,3,8,8,3,7,20,6,3])

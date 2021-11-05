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

#-------------------------------------------------------------------------------

#this function uses the extract min function to find the minimum and arranges
#xs in order from smallest to largest values, except we don't actually modify
#xs, we return another list.
def pop_sorted(xs):

    #copy list holds the copy of xs
    #ordered list holds the final ordered list of the list copy
    copy = []
    ordered = []
    
    #loop that appends all the values in xs to the list copy
    for i in range(len(xs)):
        value = xs[i]
        copy.append(value)
    
    #loop that uses extract_min to find the minimum and append it to the 
    #ordered list
    for i in range(len(copy)):
        minimum = extract_min(copy)
        ordered.append(minimum)
    
    #loop that removes each minimum one-by-one from the list copy
    for j in range(len(copy)):
        value = copy[j]
        if value == minimum:
            copy.pop(j)
        continue
    return ordered

pop_sorted([2,3,4,2,4,6,5])

#-----------------------------------------------------------------------------
#for this function, it is extremely similar to the function above, but this
#time we actually modify xs, the given list parameter.
def pop_sort(xs):
    
    #copy list holds the copy of xs
    #order_t list is temporary and holds the ordered list of xs
    copy = []
    order_t = []
    
    #loop that appends all values in xs to the list copy
    for i in range(len(xs)):
        value = xs[i]
        copy.append(value)
    
    #loop that uses extract_min to find the minimum and append it to the
    #ordered list
    for i in range(len(copy)):
        minimum = extract_min(copy)
        order_t.append(minimum)
    
    #loop that alters xs by replacing a value xs[a] with the number in the
    #ordered list that corresponds with the same index of a
    for a in range(len(xs)):
        value = order_t[a]
        
        xs[a] = value
    
    return None

pop_sort([5,1,6,2,7,3,8,4,9,0])

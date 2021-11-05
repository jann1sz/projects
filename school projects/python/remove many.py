#takes xs, removes v if its in xs by the limit. if the limit is none, we remove
#every number v from the list xs. if there is a specified limit, we only remove
#the number v from the list xs specified by the limit. 

#for example, if xs is [100,2,100,4,100,6,100,8,100,100,100,100,10,100], v is
#100, and the limit is 5, we only remove 5 of the 100s in the list xs, which
#returns [2,4,6,8,100,100,100,10,100]. if the limit was None, every 100 within
#xs would be removed. for this project, my instructor asked us to return None.

def remove_many(xs, v, limit=None):
    
    #indexmark list holds the indexes where values within the list xs are equal
    #to v
    indexmark = []

    if limit == None:

        #if the limit is equal to None, all of the numbers equal to v within the
        #list xs must be removed, so the loop will indicate and append all of
        #the indexes of the values in the list xs that equal to v.
        for i in range(len(xs)):
            value = xs[i]
            if v == value:
                indexmark.append(i)

   
    elif limit != None:
        
        #tracker is a variable that is equal to the given limit, and is
        #subtracted by 1 for every iteration until it reaches zero.
        tracker = limit
        
        for i in range(len(xs)):
            #if statement for if the limit is not equal to zero but there are
            #no more numbers within the list xs that are equal to v
            if v not in xs:
                continue
            
            #if the tracker variable is equal to zero, then we have reached our
            #given limit
            if tracker == 0:
                continue
            
            value = xs[i]
            
            #if a value within the list xs is equal to v, the index of that
            #variable is appended to indexmark for later reference
            if v == value:
                indexmark.append(i)
                tracker -= 1

    #loop that replaces all of the places where a value within the list xs is
    #equal to v with 'x' so that those slots can be simultaneously removed from
    #the list
    for i in range(len(indexmark)):
        index = indexmark[i]
        xs[index] = 'x'
            
            
    for x in xs:
    
        #if there is no 'x' within the list xs, then that means the removal of
        #all of the values within the list xs that are equal to v already
        #happened, therefore the loop breaks.
        if 'x' not in xs:
            break
        #removes all of the places where the value is 'x', which indicates the
        #places where there was a value in the list xs that was equal to v
        if 'x' in xs:
            xs.remove('x')
    
    return None

remove_many([100,2,100,4,100,6,100,8,100,100,100,100,10,100],100,5)

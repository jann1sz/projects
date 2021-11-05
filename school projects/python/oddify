#takes the list xs and finds all the even numbers. evens is an optional parameter
#which already provides a predetermined list that must be used to store all the
#even numbers. if there is no evens number, an evens list is created.

#for example, if xs is [10,20,30,40,2,4,6,7], and evens is [10000], then the
#final list will be [10000,10,20,30,40,2,4,6]. for this assignment, my instructor
#asked us to return None.

def oddify(xs, evens=None):

    #variable to reference a number in xs
    s = 0
    
    #if an evens list is not given, the function creates a list called 'even'
    #for all of the even numbers to be appended to
    if evens == None:
        even = []

    #loop that finds all of the even numbers and appends them accordingly to
    #either a given evens list or a created evens list
    for i in range(len(xs)):
        value = xs[i]
        
        #if the remainder of value divided by two is zero, then the number is
        #even and appended accordingly to an evens list
        if value % 2 == 0:
            if evens == None:
                even.append(value)
                
            elif evens != None:
                evens.append(value)
    
    #loop that changes all of the even values within the list xs to 'x' so that
    #they can easily be removed in the next loop
    
    #s value increments in both the if and else statement until it reaches the
    #length of s
    for j in range(len(xs)):
        value = xs[j]
        if value % 2 == 0:
            xs[s] = 'x'
            s+=1
        else:
            s +=1
    
    #every time the function removes an 'x' from the list xs, the length will
    #change and be subtracted by one for each 'x' that gets removed
    length = len(xs)
    for x in range(length):
        
        #if there are no more 'x' in the list xs, that means all of the even
        #numbers have been removed and therefore the loop breaks
        if 'x' not in xs:
            break
        
        #for every 'x' in xs, they must be removed, and the length of xs is
        #subtracted by one
        if 'x' in xs:
            xs.remove('x')
            length -=1
            
    
    #if there was no given evens list, we return the created list even
    if evens == None:
        return even
    
    #if there was a given evens list, we return that given evens list
    elif evens != None:
        return evens

oddify([10,20,30,40,2,4,6,7],[10000])

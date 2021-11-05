#this function takes a given array, and a parameter v. we must insert v into
#the array in correct order.

#for example, if the array is [2,4,6,8,10], and v is 5, vs becomes [2,4,5,6,8,10].
#for this assignment, we return none, but xs is modified to fit in its correct
#order when we include v.

def insert_ordered(xs,v):
    
    #indexmark is a placeholder for the index in which v would fit in in
    #regards to the list xs
    
    #leftover is a list that holds the indexes, including indexmark, from where
    #v would fit in regards to the list xs, to the last number in xs
    
    #bracket is a placeholder for the numbers that go after v
    indexmark = []
    leftover = []
    bracket = []

    #j is a variable that helps us refer to the number after a number that the
    #index i is referring to
    j = 1

    #if the list of xs is empty, append v and immediately return None without
    #going through the other unnecessary loops
    if xs == []:
        xs.append(v)
    
        return None
    

    else:
        for i in range(len(xs)):
            
            #if there is only one number in the list xs: 
            if len(xs) == 1:
                value = xs[i]
                
                #if v is larger than the value in xs, then the index would be
                #1 since the number would go after the value in xs
                if v > value:
                    indexmark.append(1)
                    
                #if v is smaller than the value in xs, then the index would be
                #0 since the number would go before the value in xs
                elif v < value:
                    indexmark.append(0)
            
            #elif we get to the last number(meaning indexmark would therefore
            #be empty), then v would be inserted as the last number, so j would
            #be appended to indexmark
            elif i == len(xs)-1 and indexmark == []:
                indexmark.append(j)
            
            #if j is equal to the length of xs, that would mean there are no
            #more numbers for us to compare to since we went through the whole
            #list
            elif j == len(xs):
                continue
            
            elif len(indexmark) > 0:
                continue
            
            #value1 accesses the first number
            #value2 accesses the number following value1
            else:
                value1 = xs[i]
                value2 = xs[j]
                
                #if v is smaller than the first accessed number and smaller than
                #the second number following, the index that v would be inserted
                #with will be the value of i
                if v < value1 and v < value2:
                    indexmark.append(i)
                
                #if v is larger than the first accessed number, but is smaller
                #than the second number following, the index that v would be
                #inserted with will be the value of j
                elif v > value1 and v < value2:
                    indexmark.append(j)

            #j must be incremented by one since the loop does not automatically
            #increment j
            j+=1

    
    #index_new refers to the indexmark(which holds the index that v would use to
    #be inserted into the list xs
    
    #length refers to the length of xs, bracket_len refers to the length of
    #bracket
    
    #eq takes the length of xs plus the length of bracket, since later there
    #will be a loop that pops all of the values that are larger than v so that
    #v can be inserted and the numbers that were popped will be appended back
    index_new = indexmark[0]
    length = len(xs)
    bracket_len = len(bracket)
    eq = (length + bracket_len)
    
    #for i in range of the index that v fits in with, length of xs:
    for i in range(index_new, length):
    
        #if len(xs) == 1, break since there are no leftovers and v can be 
        #appended in simpler terms
        if len(xs) == 1:
            break
            
        #leftover list will be appended with the indexes of v and the numbers
        #larger than v
        leftover.append(i)
        
    
    for num in range(index_new, length):
        if len(xs) == 1:
            break
        value = xs[num]
        
        #bracket list will be appended with the numbers larger than v for later
        #reference so that we can append these numbers back after they've been
        #popped for v to be inserted
        bracket.append(value)
    

    #loop that keeps removing the last number of the list xs until we reach the
    #value that is smaller than v, so that v can be appended after that value
    for i in range(len(leftover)):
        if len(xs) == 1:
            break
        xs.pop(-1)
        
    #s will be used to refer to the index of the list leftover
    s = 0

    #for x in range(index of v, eq+1 (since we're adding an extra number to xs,
    #the length gets extended by one)):
    for x in range(index_new, eq+1):
        
        #if there are no leftover numbers that need to be appended and v is
        #already in xs(which probably meant the list xs was initially empty),
        #then the loop breaks
        if len(leftover) == 0 and v in xs:
            break
        
        #if there is one number in the list leftover:
        if len(leftover) == 1:
            leftoverindex = leftover[s]
            
            #if the index in the list leftover is the same as the index that
            #refers to where v would fit in the list xs, then append v to xs
            if index_new == leftoverindex:
                xs.append(v)

            #the value in bracket(which are the numbers that we removed for v to
            #be inserted) is appended back to xs
            insert = bracket[0]    
            xs.append(insert)
            
            #pops the first value of bracket list and leftover list so that we
            #can keep track of which numbers still must be appended back to xs
            bracket.pop(0)
            leftover.pop(0)
        
        #if there is no leftovers that need to be appended but v is not in xs
        #yet:
        elif len(leftover) == 0:
            a = 0
            b = 1
            index = indexmark[0]
            value = xs[0]
            
            #if v is smaller than the only value in xs:
            if v < value:
                
                #first append v to the list (which is in its wrong order), and
                #then gets bubble sorted so that v appears first in the list,
                #and then the value appears second
                xs.append(v)
                xs[a], xs[b] = xs[b], xs[a]
            
            #if v is larger than the only value in xs, append v to xs with no
            #need to switch order of numbers
            elif v > value:
                xs.append(v)
            
        else:
            leftoverindex = leftover[s]
            insert = bracket[0]
            
            #if the index in the list leftover is the same as the index that
            #refers to where v would fit in the list xs, then append v to xs
            if index_new == leftoverindex:
                xs.append(v)
                
                #increment s by one so that it can refer to the next number in
                #the list leftover
                s+=1
            else:
            
                #append the number within bracket(which refers to the numbers
                #that we popped from xs in the beginning) and pops that number
                #from bracket so we don't append the same number more than once
                xs.append(insert)
                bracket.pop(0)

    return None

insert_ordered([10],6)

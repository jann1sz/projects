def deep_copy(some_2d_list):
    
    #new_copy list is the list that holds the copy of some_2d_list
    new_copy = []
    
    #i will reference the lists within some_2d_list, and j will reference the
    #items within each list.
    i = 0
    j = 0
    
    #loop that creates a deep copy of some 2d list
    for i in range(len(some_2d_list)):
    
        #bracket is an empty list that will append each item in the lists of
        #some_2d_list.
        
        #once all of the numbers in the first list are appended to bracket and
        #bracket is appended to the new copy list, the bracket list becomes
        #empty when it moves to the next list within some_2d_list
        bracket = []
        for j in range(len(some_2d_list[i])):
        
            #value calls the first list in some 2d list
            #single_var calls the first item in the first list
            value = some_2d_list[i]
            single_var = value[j]
            
            #each item in the list is appended to the bracket list, which will
            #then be appened to the new_copy list
            bracket.append(single_var)
        new_copy.append(bracket)
        
    return new_copy

deep_copy([[1,2],[3,4]])

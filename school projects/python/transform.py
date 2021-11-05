#takes the given data and transforms it to a new list by the defined rows and columns given by the parameters

def transform(data, num_rows, num_cols):

    #copy list holds the deep copy of the data list.
    
    #transform_list is the returned list after the data list has been
    #transformed with the given number of rows and columns.
    
    #bracket is a list that temporarily holds the items that total to the given
    #number of columns. once the length of bracket list totals the number of
    #columns, it gets appended to transform_list and becomes empty for the next
    #set of items.
    copy = []
    transform_list = []
    bracket = []
    
    #loop that creates a deep copy of the data list by appending the values in
    #data list to the copy list.
    for i in range(len(data)):
        value = data[i]
        copy.append(value)

    #length holds the length of the copied list, which tells us how many numbers
    #are in the given data list
    
    #total_num holds the total number of items there should be according to the
    #given number of rows and columns
    length = len(copy)
    total_num = num_rows * num_cols
    
    #if the number of items in data list don't equal the total number of items
    #that should be equally distributed into their respective rows and columns:
    if length != total_num:
    
        #if the length of copy is less than the total number of items that
        #would be equally distributed by the given rows and columns, the amount
        #of missing numbers is calculated with leftover.
        
        #leftover subtracts total_num with length to get the leftover amount of
        #numbers that need to be replaced with zeros
        if length < total_num:
            leftover = total_num - length
            bracket = []
            
            #during the time the length of copy is still less than the total
            #amount of numbers, zeros will be appended to replace the gaps.
            
            #length gets increased for each zero that is appended until it
            #becomes equal to total_num
            while length < total_num:
                copy.append(0)
                length +=1

        #if there are more items in the data list than the total number of items
        #that would be equally distributed by the given rows and columns, an
        #empty list is returned.
        if length > total_num:
            return []

    #loop that takes the value of copy[i] and appends it to the bracket list
    #temporarily; once the length of bracket is equal to the number of given
    #columns, the bracket list gets appended to transform_list and becomes empty
    #for the next set of items.
    for i in range(len(copy)):
        new_val = copy[i]
        bracket.append(new_val)
        if len(bracket) == num_cols:
            transform_list.append(bracket)
            bracket = []
        
    return transform_list

transform([2,4,6,8,1,3,5,7,9,0], 5, 2)

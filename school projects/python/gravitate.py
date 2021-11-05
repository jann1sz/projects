#takes the sum in each 2d array and gravitates the sum to the direction given within the parameters

#for example, if we have the 2D array [[1],[2,1],[3,2,1],[4,3,2,1],[5,4,3,2,1]], and the direction
#is "right", the output would be [[1],[0,3],[0,0,6],[0,0,0,10],[0,0,0,0,15]].




def gravitate(nums, directions):

    #manually calculating the sum instead of using sum()
    sum = 0
    length = len(nums)
    i = 0
    j = 0
    
    #loop that calculates the sum of the individual lists within nums
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            list_var = nums[i]
            item_var = list_var[j]
            
            sum += item_var
        
        #if directions is left, then the first number within the list should be
        #the sum all the numbers within the list
        if directions == 'left':
            nums[i][0] = sum
            sum = 0
            
            len_column = len(nums[i])
            
            #if the number of items within the list is 1, there will be no
            #zeros appended to the list and continues to the next list
            if len_column == 1:
                continue
                
            #if there are more than one items within the list, k = 1 because the
            #sum has already replaced the first item in the list.
            for k in range(len(nums[i])):
                k = 1
                
                #while k is less than the number of items that are in the list,
                #the numbers (besides the sum) will be replaced with zeroes
                #until all of the numbers in the list are replaced.
                while k < len_column:
                    nums[i][k] = 0
                    k +=1
                
        #elif directions is right, then the last number within the list will be
        #the sum, and the rest of the numbers are replaced with zeros
        elif directions == 'right':
            len_column = len(nums[i])
            nums[i][-1] = sum
            sum = 0
            
            #if the length of the list is 1, meaning there was only one number
            #in the list to begin with, there will be no zeros appended to the 
            #list and continues
            if len_column == 1:
                continue
                
            #k = 0 because the last number is the sum, therefore we start at the
            #beginning of the list and replace them with zeros while k is less
            #than the number of items in the list minus one(because the last
            #number is the sum)
            for k in range(len(nums[i])):
                k = 0
                while k < len_column-1:
                    nums[i][k] = 0
                    k += 1
                
            
    return nums
    
gravitate([[1],[2,1],[3,2,1],[4,3,2,1],[5,4,3,2,1]], "right")

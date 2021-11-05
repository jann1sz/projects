def sum_gt_avg(num_list):

    num_list = list(num_list)
    
   
    #the total variable is the sum of all the numbers in the list
    i = 0
    total = 0
    
    for i in range(len(num_list)):
        
        #converting the list into a float
        num_list[i] = float(num_list[i])
        
        
        total = total + num_list[i]
        
        #once all values are added up, we calculate the average
        if i == (len(num_list) - 1):
            average = total / len(num_list)
            
    
    
    #the sum variable is the sum of numbers larger than the average
    i = 0
    sum = 0
    
    #calculates the sum of numbers larger than the average
    for i in range(len(num_list)):
        
        
        if num_list[i] > average:
            sum = sum + num_list[i]
            
            #once all values are added to sum, loop breaks
            if i == (len(num_list) - 1):
                break
            

        else:
            i = i + 1
            
    return sum




sum_gt_avg('12345')

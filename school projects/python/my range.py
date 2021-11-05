#function that gives a start and end point x&y, and increases or
#decreases depending on z, which may or may not be given.

#for example, if these are the parameters: (20,0,-3), this means
#the start point is 20, the end point is 0, and it decreases in
#decrements of 3. so the list we get is [20,17,14,11,8,5,2]. since
#2-3==-1, 2 becomes the last number of the list.

def my_range(x,y=0,z=1):
    
    #range_list is the list where the ranges will be appended to
    range_list = []
    
    #if there is no given y value, then the given x value is the stop, start
    #will be assigned to y which holds the value of zero, and step will be
    #assigned to z which holds the value of 1
    if y == 0:
        stop = x
        start = y
        step = z
    
    #if there is a given y value or z value (if there is a value for z, then
    #that means all values of x,y, and z are given), then start will be assigned
    #to x, stop will be assigned to y, and step will be assigned to z
    if y != 0 or z!= 1:
      start = x
      stop = y
      step = z
 

    #if the start value is less than stop,
    if start < stop:
    
        #if step is a positive number, then append the start number to the list
        #range_list
        if step > 0:
            range_list.append(start)
            
        #the range starts with start+1 since the function has already appended
        #the start value to the list range_list
        for i in range(start+1, stop):
            
            #if step is smaller than zero and the value of start is less than
            #stop, the loop breaks since it's not possible to reach stop if
            #step is negative while start is trying to reach stop
            if step < 1:
                break
                
            #eq is the equation of start plus step, where the start value will
            #be replaced with eq once the equation has been appended to the list
            #range_list
            eq = start + step
            
            #if start is equal to stop, there is no need for any more numbers to
            #be appended, and therefore the loop breaks
            if start == stop:
                break
            
            #if the next step of the equation of start + step is larger than
            #stop, there is no need for any more numbers larger than step to be
            #appended, and therefore the loop breaks
            elif start + step > stop:
                break
            range_list.append(eq)
            start = eq
            
    #if start is larger than stop,
    elif start > stop:
        
        #if step is a negative value and start is larger than stop, append the
        #start value to the list range_list
        if step < 0 and start > stop:
            range_list.append(start)
        
        for i in range(stop+1, start):
            
            #if step is a positive number while start is larger than stop, then
            #it would not be possible for start to ever reach stop, and there-
            #fore the loop breaks
            if step > 0:
                break
            
            #eq is the same equation as the if statement prior to this elif
            #statement, and would work the same even if step was negative
            eq = start + step
            
            #if the equation is equal to the stop value, there is no need for
            #any more numbers smaller than stop that should be appended to the
            #list range_list, and therefore the loop breaks
            if eq == stop:
                break
            
            #if start + step (in terms of this, since step is a negative number,
            #then its essentially start - step) is smaller than stop, there is
            #no need for any more numbers smaller than stop that should be
            #appended to the list range_list, and therefore the loop breaks
            elif start + step < stop:
                break
            
            range_list.append(eq)
            start = eq
        
    return range_list

my_range(0,-10,-2)

#function that takes a 2D array and adds each component by the given amount.

#for example, if the grid is [[1,3,5],[1,2,3,4,5],[],[6],[-1,-3,-2]], and the
#amount is 2, the grid then becomes [[3,5,7],[3,4,5,6,7],[],[8],[1,-1,0]].

def inc_all(grid, amount=1):
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
        
            #list_var accesses the lists within grid
            #item_Var accesses the individual items within those lists of grid
            list_var = grid[i]
            item_var = list_var[j]
            
            #added is an equation that takes the items in the lists within grid
            #and adds the amount(the given one or the standard amount of 1)
            
            #the individual items within these lists are then replaced with
            #the added result
            added = item_var + amount
            list_var[j] = added
    
    return None
    
    
inc_all([[1,3,5],[1,2,3,4,5],[],[6],[-1,-3,-2]],2)

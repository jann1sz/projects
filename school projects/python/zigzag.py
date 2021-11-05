def zigzag(text):
    i = 0
    total_length = len(text)
    
    #new zigzag word
    new_word=''
    
    for i in range(len(text)):
        
        #if the text has an odd number of characters
        if len(text) % 2 == 1:
            
            new_word = new_word + text[i]
            total_length = total_length - 1
        
        
            #once all of the words are in the new zigzag word,
            #the loop stops
            if total_length < 1:
                break
               
            new_word = new_word + text[(-i)-1]
            total_length = total_length - 1
            
            
        #else if the text has an even number of characters    
        elif len(text) % 2 == 0:
            
            
            #once all of the words are in the new zigzag word,
            #the loop stops
            
            if total_length < 1:
                break
            
            
            new_word = new_word + text[i]
            total_length = total_length - 1
        
               
            new_word = new_word + text[(-i)-1]
            total_length = total_length - 1  
        
    return new_word        


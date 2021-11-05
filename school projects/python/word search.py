
#the puzzle list parameter is the list of words we look at to see if any
#words in the words list show up within the puzzles list

def word_search(puzzle, words):
    
    #puzzlec and wordsc are deep copies of the puzzle and words lists
    puzzlec = []
    wordsc = []
    
    #puzzleh is a placeholder for when we convert puzzlec to a list of 
    #characters, the string items in puzzleh are separated and become a list of 
    #alphabetical characters
    puzzleh = []
    
    #bracket is a temporary list that holds the characters while it's being
    #converted to backwards order
    #word_temp holds the list of individual characters within a word in
    #backward order
    bracket = []
    word_temp = []
    
    #words that appear in puzzle (in any order)
    appear = []
  
    #backwards list shows the words in puzzle where each word is in backwards
    #order
    backwards = []
    
    #z variable to get the negative index in order to print words backwards
    z = 1
    
    #final_order is the list of words that appear in puzzle but in its proper
    #order
    final_order = []
    
    #loops that make the deep copy of puzzle list and words list
    for i in range(len(puzzle)):
        value = puzzle[i]
        puzzlec.append(value)    
    for i in range(len(words)):
        value = words[i]
        wordsc.append(value)

    #list that checks for words that appear in puzzle, when the words in the
    #puzzle copy are analyzed from left to right
    for i in range(len(puzzlec)):
        for j in range(len(wordsc)):
            value1 = puzzlec[i]
            value2 = wordsc[j]
            
            if value2 in value1:
                appear.append(value2)

    #loop that puts the copy of puzzle in a placeholder to convert these words
    #in backwards order
    #list_ver creates a list of the words but each character in the word
    #becomes its own item
    for i in range(len(puzzlec)):
        list_ver = list(puzzlec[i])
        puzzleh.append(list_ver)

    #loop that takes the negative index of the word and adds to bracket, and
    #once each character is added in backwards order, it gets appended to
    #word_temp and the bracket list is emptied, as well as the z variable, which
    #once again becomes 1
    for j in range(len(puzzleh)):
        for k in range(len(puzzleh[j])):
            k -= z
            
            #list_var accesses the lists in the copy of puzzles
            #item_var accesses the items in the lists in the copy of puzzles
            list_var = puzzlec[j]
            item_var = list_var[k]
            bracket.append(item_var)
            z+=2
        word_temp.append(bracket)
        bracket = []
        z = 1
    
    j = 0
    #loop that takes each list within word temp and stitches the individual 
    #characters within the list to create the backwards ordered word
    for i in range(len(word_temp)):
        separator = ''
        value = word_temp[i]
        item = value[j]
        new = separator.join(value)
        backwards.append(new)
        j+=1
    print(backwards)

    #loop that checks for words that appear in puzzle, when the words in the 
    #puzzle copy are analyzed from right to left.
    for i in range(len(backwards)):
        for j in range(len(wordsc)):
            value1 = backwards[i]
            value2 = wordsc[j]
            
            if value2 in value1:
                appear.append(value2)
    
    #loop that takes the copy of words and compares it to the words that appear
    #in the copy of puzzles and appends the words that appear in puzzles to a
    #final list in its original preserved order
    for i in range(len(wordsc)):
        for j in range(len(appear)):
            value1 = wordsc[i]
            value2 = appear[j]
            
            if value1 in value2:
                final_order.append(value1)
  
    #returns the final order of words that appear in puzzle in order, without
    #any duplicates
    final_order_set = set(final_order)
    return final_order_set

word_search(["BATE"], ["ATE","TAB","FUR"])

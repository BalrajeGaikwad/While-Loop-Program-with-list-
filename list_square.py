#Now we give code examples of while loops in Python for square every number of a list. The code is given below -

list_ = [3, 5, 1, 4, 6]    
squares = []    
 
while list_:   
    squares.append( (list_.pop())**2)     
print( squares )    
def mult(a,b):
    
    result = 0
    
    while b > 0:
        
        result += a
        
        b -= 1
        
    return result
        

mult = mult(3,100)

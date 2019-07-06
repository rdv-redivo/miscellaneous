def mult(a,b):
    
    result = 0
    
    while b > 0:
        
        result += a
        
        b -= 1
        
    return result

def iterPower(base, exp):
    
    total = 1
    
    for i in range(exp):
    
        total *= base
        
    return total
        
total = iterPower(5,3)
    
mult = mult(3,100)

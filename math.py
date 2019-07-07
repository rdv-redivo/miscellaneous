'''
Is a recursive function a replicant?:-)
'''
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

def recurPower(base, exp):
 
    if exp == 0:
        return 1

    return base * recurPower(base, exp - 1)
    
totalPowerRec = recurPower(0,2)
        
totalPower = iterPower(5,3)
    
totalMult = mult(3,100)

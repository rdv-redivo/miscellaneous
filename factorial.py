def fatorial(n):

    if n == 1 or n == 0:
        
        return n

    return n * fatorial( n - 1 )
    
#Example
fatorial = fatorial(5)

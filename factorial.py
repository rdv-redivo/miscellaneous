def fatorial(n):

    if n == 2:
        
        return n

    return n * fatorial( n - 1 )
    
#Example
fatorial = fatorial(5)

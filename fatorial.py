def fatorial(n):

    if n == 1:
        
        return n

    return n * fatorial( n - 1 )
    
#Example
fatorial = fatorial(5)

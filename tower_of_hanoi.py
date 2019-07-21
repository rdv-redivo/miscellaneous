#Tower of Hanoi - Recursive Method

def hanoi(n, origem, aux, destino):
    
    if (n == 1):
        
        print('Mova de', origem,'para', destino, '.')
    
    else:
            
        hanoi(n-1, origem, destino, aux)
        hanoi(1, origem, aux, destino)
        hanoi(n-1, aux, origem, destino)
        
        
#hanoi(10 , 'P1', 'P2', 'P3')

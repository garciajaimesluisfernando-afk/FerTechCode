def piramide(n):
    
    if n == 0:
        return 
    
    
    piramide(n - 1)
    print(str(n) * n)
    return 
    
    
print(piramide(5))
def media_piramide(n):
    
    
    if n == 1:
        return 1
    
    
    print(str(n) * n)
    
    
    return media_piramide(n - 1)
        
        
    

    


print(media_piramide(5))
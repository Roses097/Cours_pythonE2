

def syra(n):
    print(n)
    if (n % 2) == 0:
        n = n//2
        
    else:
        n = (n*3)+1
        
    return (syra(n))

syra(5)


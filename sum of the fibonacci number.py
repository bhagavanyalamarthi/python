def nearfib (n):
    a,b=0,1
    while n>=b:
        if n==b:
            return b
        a,b=b,a+b
    print(a)
    return nearfib(n-a)

n=int(input("enter a number"))
print(nearfib(n))

        
    
        

def nearfib(n):
    a,b=0,1
    while b<=n:
        c=a+b
        a=b
        b=c
        print(a,b)
    if abs(n-a)<abs(n-b):
         return a
    else:
         return b
n=int(input("enter a num"))
print(nearfib(n))

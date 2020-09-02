def beforefib(n):
    a,b=0,1
    while b<=n:
        c=a+b
        a=b
        b=c
    return a
n=int(input())
print(beforefib(n))


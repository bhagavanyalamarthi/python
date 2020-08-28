def prime (n):
        for i in range (2,n):
            if n % i==0:
                break
        else:
            return (1)
n=int(input("enter a number"))
ctn=0
while prime(n) and n>0:
    n=n//10
    if prime(n):
        ctn=1

    else:
        ctn0
if ctn==1:
    print(n,"right truncated ")
else:
    print(n,"not truncated")

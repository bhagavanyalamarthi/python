def prime (n):
        for i in range (2,n):
            if n % i==0:
                break
        else:
            return (1)
n=int(input("enter a number"))
ctn=0
if(prime(n)==1):
    print(n,"is prime")
    for i in range(2,n+1):
        if (prime(i)==1):
            ctn+=1
    if (prime(ctn)==1 and n>2):
        print(n,"is super prime")
    else:
        print(n,"is not super prime")
else:
    print(n,"is not prime")

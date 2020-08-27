def prime (n):
 for i in range (2,n+1):
    if n % i==0:
         return("is not a prime number")
         break
    else:
       return ("is  prime")

    
n=int(input("enter a number"))
print(prime(n))
def near_prime(n):
    n1=n-1
    while True:
        if prime(n1):
            return n1
        else:
            n1-=1
n=int(input("enter a number"))
if prime(n):
    a=near_prime(n)
    b=near_prime(a)
    while True:
        if a+b+1==n:
            print(n,"is a special prime")
            break
        else:
            a=b
            b=near_prime(a)
            print(a,b)
        if a==2 or b==2:
            break
else:
    print("not special prime")
  


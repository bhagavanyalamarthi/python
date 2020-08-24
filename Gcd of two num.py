def computeGcd(a,b):
    if b==0:
        return a
    else:
        return computeGcd(b,a%b)
n1=int(input("enter a number"))
n2=int(input("enter a number"))
print(computeGcd(n1,n2))

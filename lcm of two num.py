def compute_gcd(a,b):
    if b==0:
        return a
    else:
        return compute_gcd(b,a%b)
n=int(input("enter a number"))
m=int(input("enter a number"))
lcm=(n*m)//compute_gcd(n,m)
print(lcm)

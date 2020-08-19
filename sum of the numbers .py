def sum_digits(n):
    sum=0
    while n>0:
        rem=n%10
        sum+=rem
        n//=10
    return sum
n=int(input("enteer a number"))
print(sum_digits(n))

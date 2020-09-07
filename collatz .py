##collatz means for example given number 8
#it is even divided by 2 otherwise n*3+1    (8 ,4,2,1) it is equal to 1 break 
n=int(input("enter a number"))
def Collatz(n):
    while n>1:
          if n%2==0:
                n//=2
                print(n, end=' ')
          else:
                n=n*3+1
                print(n,end=' ')

Collatz(n)

co

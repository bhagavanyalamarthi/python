import math
def beatty(n):
    for i in range (1,n+1):
        value=math.floor(i*math.sqrt(2))
        print(value)
n=int(input("enter a num"))
beatty(n)

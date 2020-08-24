n=int(input("enter a number"))
a=0
b=0
for i in range(2,n+1):
  c=a+b
  a=b
  b=a
print(b, end=" ")

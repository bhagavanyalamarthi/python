#example given number=6
#first find out factors of given num
#if factors==given num print true r false(6 factors 1,2,3,factors 1+2+3=6 s0 factors=num))
def xyz(n):
 
    c=0

    for i in range(1,n):

          if n%i==0:
      
              c+=i

                   #print(c)

    if c==n:

            return "True"

    else:

            return "False"
n=int(input())
print(xyz(n))

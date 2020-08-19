def arm_num(n):
    arm=0
    n1=n
    while n>0:
        rem=n%10
        arm+=rem*rem*rem
        n//=10
    if n1==arm:
        return("armstrong")
    else:
        return("not a armstrong")
n=int(input("enter a num"))
print(arm_num(n))


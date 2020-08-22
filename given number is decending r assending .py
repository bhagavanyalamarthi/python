n=input("enter a number")
asc=n[0] <= n[1]
dsc=n[0] >= n[1]
i=1
while (i<(len(n)-1)):
    if asc:
        asc =n[i] <= n[i+1]
    elif dsc:
        dsc = n[i] >= n[i+1]
    else:
        break
    i+-1
if asc:
    print("ascending")
elif dsc:
    print("decending")
else:
    print("not found")

marksheet=[]
marklist=[]
n=int(input())
for i in range(n):
    name=input()
    marks=float(input())
    record=[name,marks]
    marksheet.append(record)
    marklist.append(marks)
marksheet.sort()
secondLowestScore=sorted(set(marklist))[1]
for i,j in marksheet:
    if j==secondLowestScore:
        print(i)



Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry

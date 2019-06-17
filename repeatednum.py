a=int(input())
b=list(map(int,input().split()))
c=[]
for x in range(a):
    for i in range(x+1,len(b)):
        if(b[i]==b[x]):
          c.append(b[x])
if (len(c)==0):
    print("unique")
else:
    c.sort()
    l1=set(c)
    for x in l1:
        print(x,end=" ")

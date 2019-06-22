from itertools import combinations
x,y=map(int,input().split())
l1=list(map(int,input().split()))
p=[]
q=0
for i in range(1,x):
    d1=combinations(l1,i)
    for j in list(d1):
        if(sum(j)==y):
            q=q+1
if(q>=1):
    print("yes")
else:
    print("no")

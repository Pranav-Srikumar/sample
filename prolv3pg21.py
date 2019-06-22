import statistics as stat
p=int(input())
list1=list(map(int,input().split()))
q=0
for i in range(1,p):
    l1=lisst1[0:i]
    l2=list1[i:p]
    if(stat.mean(l1)==stat.mean(l2)):
        q=q+1
if(q>=1):
    print("yes")
else:
    print("no")

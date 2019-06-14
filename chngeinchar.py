a,b=input().split()
cnt=0
for i in range(0,len(a)):
    if(a[i]!=b[i]):
        cnt=cnt+1
if(cnt==1):
    print("yes")
else:
    print("no")

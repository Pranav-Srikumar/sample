a=int(input())
b=list(map(int,input().split()))
c=0
for i in range(len(b)-2):
    for x in range(i+1,len(b)-1):
         for j in range(x+1,len(b)):
            if b[i]<b[x]<b[j] and i<x<j:
                c+=1
print(c)    

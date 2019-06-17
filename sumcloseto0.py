a=int(input())
b=list(map(int,input().split()))
c=max(b)
d,e=0,0
for i in range(0,len(b)):
  for j in range(i+1,len(b)):
    if abs(b[i]+b[j])<l:
      d,e=b[i],b[j]
      c=abs(d+e)
print(d,e)

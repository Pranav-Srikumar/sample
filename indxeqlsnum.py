a=int(input())
b=list(map(int,input().split()))

c=[]
for i in range(a):
	if b[i]==i:              
		c.append(i)
		
if len(c)==0:
	print(-1)
else:
	for i in c:
		print(i,end=" ")

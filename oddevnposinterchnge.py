a=int(input())
b=list(map(int,input().split()))
c=[]

for i in range(a):
	if i%2!=0 and b[i]%2==0:  
		c.append(b[i])
	if i%2==0 and b[i]%2!=0:  
		c.append(b[i])
for i in c:
	print(i,end=" ")

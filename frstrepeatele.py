a=int(input())
l1=list(map(int,input().split()))
c=[]
for i in l1:
	if l1.count(i)>1:
		c.append(i)                   
		
if len(c)==0:
	print('unique')
els:
	c.reverse()                           
	x=max([c.index(i) for i in c])        
	print(c[x])

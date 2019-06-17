a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
flag=0
for i in l2:
	if i not in l1:
		flag=1
		break
if flag==0:
	print('YES')
else:
	print('NO')

a,b=map(int,input().split())
for i in range (a+1,b):
  temp=i
  sum=0
  while(temp>0):
    remainder=temp%10
    sum=sum+remainder**3
    temp=temp//10
  if(i==sum):
    print(i,end=' ')

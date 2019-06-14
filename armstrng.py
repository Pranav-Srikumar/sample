num=int(input())
temp=num
sum=0
while(num>0):
  k=num%10
  num=num//10
  c=k**3
  sum=sum+c
if(temp==sum):
  print('Armstrong num')
else:
  print('not an armstrong')

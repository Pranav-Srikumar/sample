import math
num=int (input())
for i in range(num):
    a=math.factorial(2*i)
    b=math.factorial(i+1)
    c=math.factorial(i)
    d=a//(b*c)
    print(d,end=' ')

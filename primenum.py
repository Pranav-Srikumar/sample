a=int(input())
b=int(a/2)
for i in range(2,b+1):
  if (a%i==0):
    print("not prime")
    break
else:
    print("its prime")

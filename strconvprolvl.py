a,b=input().split()
A=abs(len(a)-len(b))
for i in range(len(a)):
    if len(b)==1 and b[i] in a:
        break
    if a[i]!=b[i]:
        A+=1
print(A)

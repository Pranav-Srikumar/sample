n=list(map(int,input().split()))
k=list(map(int,input().split()))
sum=0
for i in range(n[1]):
    sum=sum+k[i]
print(sum)

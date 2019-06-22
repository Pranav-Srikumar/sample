x=int(input())
l1=list(map(int,input().split()))
l1=[bin(i)[2:]for i in l]
l1.sort()
l1=l1[::-1]
y=[int(i,2) for i in l1]
for i in y:
    print(i)

n=int(input())
list1=list(map(int,input().split()))
list1.sort()
med=list1[int(n/2)]
print(med)

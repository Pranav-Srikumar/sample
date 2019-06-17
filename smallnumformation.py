from itertools import combinations
str1,n1=map(int,input().split())
a1=len(str(str1))
L1=list(combinations(str(str1),a1-n1))
L1=(sorted(L1))
a="".join(L1[0])
print(a)

a=int(input())
b=[int(x) for x in input().split()]
c=[]
d=sorted(b)
while len(d)!=0:
    if len(d)!=1:
        c.append(d[-1])
        c.append(d[0])
        m.remove(d[0])
        m.remove(d[-1])
    else:
        c.append(d[0])
        d.remove(d[0])
print(*c)

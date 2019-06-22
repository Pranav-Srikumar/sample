p=input()
q=input()
r="abcdefghijklmnopqrstuvwxyz"
s=[]
t=[]
u=""
for i in range(0,len(p)):
    for j in range(0,len(r)):
        if p[i]==r[j]:
            s.append(j+1)
        if q[i]==r[j]:
            t.append(j+1)
for k in range(0,len(s)):
    tot=d[k]+e[k]
    if(tot<=26):
        u=u+c[tot-1]
    else:
        m=tot-26
        u=u+c[m-1]
print(u)
        

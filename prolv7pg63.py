p=input()
q=''
r=[]
for i in p:
    if i not in r:
        q+=i
        r.append(i)
    elif i in r:
        break
print(len(r))

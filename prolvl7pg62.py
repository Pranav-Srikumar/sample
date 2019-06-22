m=input()
sub=""
n=0
o=[]
if m==m[::-1]:
  o.append(0)
for y in range(len(m)-1):
  for z in range(y+1,len(m)):
    sub=m[y:z+1]
    if sub==sub[::-1]:
      o.append(len(m)-len(sub))
print(min(o))

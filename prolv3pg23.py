ip=raw_input()
l1=["GLGLGL","GRRG","GLLG","GRGRGR"]
cnt=0
for i in range(0,len(l1)):
    if l1[i] in ip:
        cnt+=1
if cnt==1:
    print("yes")
else:
    print("no")

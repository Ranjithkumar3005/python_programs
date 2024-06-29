s = "ekw"
u=[0] * 8
k=0
m=[]
value=False
for i in range(0,len(s)-1):
    if s[i]!=s[i+1]:
        m.append(s[i])
        for j in m:
            if j!=s[i]:
                value=True
        if value:
            u[k]+=1
    else:
        k+=1
        continue
u=sorted(u)
print(u)
print(u[7])
s = "                "
t=1
for i in range(0,len(s)-1):
    if s[i]==" " and s[i+1]!=" ":
        t+=1
s=s.strip()
if s=="":
    t=0
print(t)
s = "hehhhhhhe"
t=""
a=0
check=True
for i in range(0,len(s)):
    if s[i]==" ":
        k=s[a:i]
        k=k[::-1]
        t=t+" "+k
        a=i+1
        check=False
        
a=len(s)     
for i in range(len(s)-1,0,-1):
    if s[i]==" ":
        k=s[a:i:-1]
        print(k)
        t=t+" "+k
        break
        
if check==True:
    t=s[::-1]
    
print(t.strip())
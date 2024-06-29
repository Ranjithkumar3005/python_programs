s = "leet2code3"
k = 10
t=""
a=0
for i in range(0,len(s)):
    print(s[i])
    if s[i].isdigit():
        m=int(s[i])
        print(m)
        if t=="":
            for j in range(0,m):
              t+=s[0:(i)]
        
f=t          
for i in range(0,len(t)):
    if t[i].isdigit():
        f=f.replace(f[i],'',1)
print(f)
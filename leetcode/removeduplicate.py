s = "cbacdcbc"
f=s
for i in range(0,len(s)-1):
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            f=f.replace(s[i],'',1)
            break
print(f)     
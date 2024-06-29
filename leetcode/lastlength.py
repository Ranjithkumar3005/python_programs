s = "d"
s=s.strip()
s=s[::-1]
t=0
for i in range(0,len(s)):
    if s[i]==" ":
        break
    t+=1
  
print(t)
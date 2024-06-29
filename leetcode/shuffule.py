s = "abc"
indices = [0,2,1]
t=[0]*len(indices)
print(t)
for i in range(0,len(indices)):
    t[indices[i]]=s[i]
    
print(t)
f=""
for i in range(0,len(t)):
    f+=t[i]
    
print(f)
    

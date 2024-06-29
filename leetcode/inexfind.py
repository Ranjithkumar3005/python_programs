haystack = "sabutsad"
needle = "sad" 

a=0
b=0

for i in range(0,len(needle)):
    for j in range(a,len(haystack)):
        if needle[i]==haystack[j]:
            a=j
            b+=1
            break
        if needle[i]!=haystack[j]:
            #a=j
            b=0
            break
        
        if b==len(needle):
            break
if b!=len(needle):
     print("-1")
else:    
    print(a-b+1)
strs = ["dog","racecar","car"]
stm=strs[0]
st=""
a=0
b=0
c=0
d=0
for i in range(1,len(strs)):
    for j in range(0,len(strs[i])):
        c+=1
        d+=1
        if c==len(stm) or d==len(strs[i]):
                break
        if stm[j]==strs[i][j]:
            st+=strs[i][j]
            a+=1
            b+=1
            if a==len(stm) or b==len(strs[i]):
                break
    stm=st
    st=""
print(stm)
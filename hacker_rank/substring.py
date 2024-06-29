a="ABCDCD"
b="CDC"
count=0
no=False
for i in range(0,len(a)-1):
    for j in range(0,len(b)):
        if b[j]==a[i]:
            if b[j+1]==a[i+1]:
                if b[j+2]==a[i+2]:
                    count+=1
                    print(count)
                    no=True
        if no:
            break
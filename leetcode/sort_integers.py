arr = [0,1,2,3,4,5,6,7,8]

for i in range(0,len(arr)):
    dummy=bin(arr[i])
    for j in range(0,len(dummy)):
        if dummy[j]=='1':
            count+=1
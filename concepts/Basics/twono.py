


mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]

store=[0,0,0,0,0]
store1=[0,0,0,0,0]
for i in range(0,len(mat)):
           for j in range(0,len(mat[i])):
                if mat[i][j]==1:
                    store[i]+=1
store1=sorted(store)
for i in range(0,len(store)):
    if j in range(i,len(store1)):
        if store[i]==store1[j]:
            print(i)
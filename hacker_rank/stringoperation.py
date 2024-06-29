
def cal(strs):
    
    strs=strs.split(" ")
    if strs[0]=="insert":
        print(strs[1],strs[2])
        a.insert(int(strs[1]),int(strs[2]))
        print(a.insert(int(strs[1]),int(strs[2])))
    
    if strs[0]=="print": 
        print(a)
    if strs[0]=="remove":
        a.remove(strs[1])
    if strs[0]=="sort":
        a=sorted(a)
    if strs[0]=="append":
        a.append(strs[1])
        print(a)
    if strs[0]=="reverse":
        a=reversed(a)
    if strs[0]=="pop":
        a.pop()
        
        
            
        

if __name__ == '__main__':
    N = int(input())
    for i in range(0,N):
        strs=str(input())
        cal(strs)
    
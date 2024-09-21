def check(val,n):
    c=0
    ans=0
    for i in range(0,len(val)):
        if val[i]>n:
            c+=1
        else:
            ans+=c
        
    print(ans)
    

# Example usage
T = int(input())
for _ in range(T):
    n=int(input())
    val=list(map(int, input().split()))
    check(val,n)
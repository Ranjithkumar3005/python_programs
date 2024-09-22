def check(nums,k):
    if len(nums)==1:
        print("YES")
        return 
    nums=sorted(nums)
    val=nums[0]
    for i in range(1,len(nums)):
        if nums[i]+val<=k:
            continue
        else:
            print("NO")
            return
    print("YES")


T = int(input())
for _ in range(T):
    d = list(map(int, input().split()))
    A = list(map(int, input().split()))
    check(A,d[1])
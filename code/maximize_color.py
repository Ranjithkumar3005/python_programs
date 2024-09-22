def check(nums):
    c=0
    for i in nums:
        if i!=0:
            c+=1
    if nums[0]>1 and nums[1]>1:
        c+=1
        nums[0]-=1
        nums[1]-=1
    if nums[1]>1 and nums[2]>1:
        c+=1
        nums[1]-=1
        nums[2]-=1
    if nums[2]>1 and nums[0]>1:
        c+=1
        nums[0]-=1
        nums[2]-=1
    print(c)

T = int(input())
for _ in range(T):
    d = list(map(int, input().split()))
    check(d)
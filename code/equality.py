def check(nums):
    sum1=sum(nums)
    a=sum1//(len(nums)-1)
    res=[]
    for i in nums:
        res.append(str(i-a))
    print(" ".join(res))
T = int(input())
for _ in range(T):
    val=int(input())
    A = list(map(int, input().split()))
    check(A)
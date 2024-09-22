# cook your dish here
def check(nums):
    dum1=[]
    dum2=[]
    tot=[]
    for i in range(0,len(nums)):
        dum1.append(nums[i][:2])
        dum2.append(nums[i][2:])
    dum2=dum2[::-1]
    for i in range(0,len(nums)):
        tot.append(dum1[i]+dum2[i])
    for i in tot:
        print(" ".join(i))
        

T = int(input())
for _ in range(T):
    N = int(input())
    res=[]
    for j in range(N):
      A = input().split()
      res.append(A)
    check(res)
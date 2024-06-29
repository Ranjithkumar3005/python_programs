nums=[2,1,3,4,4]
nums=sorted(nums)
print(nums)
for i in range(0,len(nums)-1):
        if nums[i]==nums[i+1]:
            print(nums[i])
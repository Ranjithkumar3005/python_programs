nums = [2,3,6,1]

word=True
if nums[0]<nums[len(nums)-1]:
    for i in range(0,len(nums)-1):
        if nums[i]<=nums[i+1]:
            word=True
        else:
            word=False
            break
        
if nums[0]>nums[len(nums)-1]:
    for i in range(0,len(nums)-1):
        if nums[i]>=nums[i+1]:
            word=True
        else:
            word=False
            break
        
print(word)
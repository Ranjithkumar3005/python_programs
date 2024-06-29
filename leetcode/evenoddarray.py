nums = [0]
num1=[]
for i in range(0,len(nums)):
    if nums[i]%2==0:
        num1.append(nums[i])
        
for i in range(0,len(nums)):
    if nums[i]%2!=0:
        num1.append(nums[i])
        
print(num1)
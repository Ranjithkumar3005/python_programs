nums = [3,1,4,2]
n=len(nums)

def fun(nums,n):
    for i in range(n):
         for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[k] < nums[j] and nums[k] > nums[i]:
                    return True
    return False
    
    
    


if fun(nums,n):
    print("True")
else:
    print("False")

    
    
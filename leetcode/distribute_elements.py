class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr1=[nums[0]]
        arr2=[nums[1]]
        for i in range(2,len(nums)):
            if arr1[len(arr1)-1]>=arr2[len(arr2)-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        print(arr1+arr2)
        
        
        

s=Solution()
s.resultArray(nums = [5,4,3,8])
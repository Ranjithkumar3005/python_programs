nums = [4,2,5,3]
class Solution():
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        value=False
        new_first=sorted(nums)
        New_list = new_first.copy()
        New_list.reverse()
        length=len(nums)-1
        if (New_list[0]-new_first[0])==length:
            for i in range(0,len(nums)-1):
                if nums[i]==nums[i+1]:
                    print("h")
        
        

s=Solution()
s.minOperations(nums)
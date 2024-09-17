class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        val=set(nums)
        l_str=0
        
        for num in nums:
            str1=1
            current = num
        
            while (current ** 2) in val:
                current = current ** 2
                str1 += 1
        
            if str1 >= 2:
                l_str = max(l_str, str1)
        
        return l_str if l_str>=2  else -1
        
        

s=Solution()
print(s.longestSquareStreak(nums = [4,3,6,16,8,2]))
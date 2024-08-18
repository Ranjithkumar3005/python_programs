class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        for i in nums:
            str1=str(i)
            if len(str1)%2==0:
                c+=1
        print(c)
        

s=Solution()
s.findNumbers(nums = [12,345,2,6,7896])
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h=0
        zero=0
        one=0
        for i in nums:
            if i==0:
                zero+=1
            else:
                one+=1
                
            if zero==one and zero+one>h:
                h=zero+one
        return h
        
s=Solution()
print(s.findMaxLength([0,1,0]))
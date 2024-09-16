class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dum=set()
        
        while nums!=[]:
            min1=min(nums)
            nums.remove(min1)
            max1=max(nums)
            nums.remove(max1)
            dum.add((min1+max1)/2)
        print(len(dum))


s=Solution()
s.distinctAverages(nums = [9,5,7,8,7,9,8,2,0,7])
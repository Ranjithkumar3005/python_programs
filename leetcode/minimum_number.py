class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dummy=[]
        while len(nums)!=0:
            dummy1=min(nums)
            nums.remove(dummy1)
            dummy2=min(nums)
            nums.remove(dummy2)
            dummy.append(dummy2)
            dummy.append(dummy1)
        print(dummy)
        
s=Solution()
s.numberGame(nums = [5,4,2,3])
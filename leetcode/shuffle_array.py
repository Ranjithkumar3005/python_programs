class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        dum=[]
        for i in range(0,n):
            dum.append(nums[i])
            dum.append(nums[i+n])
        print(dum)
            
        
        

s=Solution()
s.shuffle(nums = [2,5,1,3,4,7], n = 3)
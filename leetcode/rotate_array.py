class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        dum=[0]*len(nums)
        k%=len(nums)
        c=0
        for i in range(0,len(nums)):

            if i+k>=len(nums):
                dum[c]=nums[i]
                c+=1
            else:
                dum[i+k]=nums[i]
        print(dum)
        '''n = len(nums)
        k %= n  # In case k is greater than n
        
        # Rotate the array using slicing
        nums[:] = nums[-k:] + nums[:-k]'''

s=Solution()
s.rotate( nums =[1,2], k = 3)
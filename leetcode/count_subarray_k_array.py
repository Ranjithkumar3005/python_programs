class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h={}
        c=0
        for i in range(0,len(nums)):
            for j in range(i,len(nums)): 
                if nums[j] in h:
                    h[nums[j]]+=1
                else:
                    h[nums[j]]=1
                if max(h.values())>=k:
                    print(h)
                    c+=1
            h={}
        print(c)
        
s=Solution()
s.countSubarrays(nums =[61,23,38,23,56,40,82,56,82,82,82,70,8,69,8,7,19,14,58,42,82,10,82,78,15,82], k = 2)
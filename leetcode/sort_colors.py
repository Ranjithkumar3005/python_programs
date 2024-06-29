class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        h={}
        for i in nums:
            if i not in h:
                h[i]=1
            else:
                h[i]+=1
        dum=[]
        for i in range(0,len(h)):
            for j in range(0,h[i]):
                dum.append(i)
        print(dum)
                
        
        
s=Solution()
s.sortColors(nums = [2,0,2,1,1,0])
class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        h={}
        for i in nums:
            if i not in h:
                h[i]=1
            else:
                h[i]+=1
        so = sorted(h, key=lambda k: (h[k], -k))
        dum=[]
        for i in so:
            for j in range(0,h[i]):
                dum.append(i)
        print(dum)
            
        
s=Solution()
s.frequencySort(nums = [1,1,2,2,2,3])
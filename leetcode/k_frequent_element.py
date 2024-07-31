class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        h={}
        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        so = sorted(h.items(), key=lambda x: x[1], reverse=True)
        dum=[]
        for i in range(0,k):
            dum.append(so[i][0])
        print(dum)
        
        

s=Solution()
s.topKFrequent(nums = [1,1,1,2,2,2,2,2,3], k = 2)
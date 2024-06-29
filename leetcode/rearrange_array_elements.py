class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos=[]
        neg=[]
        for i in nums:
            if i>=0:
                pos.append(i)
            else:
                neg.append(i)
        ans=[]
        for i in range(0,len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])
        print(ans)
        
        
s=Solution()
s.rearrangeArray( nums = [3,1,-2,-5,2,-4])
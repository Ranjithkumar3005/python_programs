class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        h1={}
        h2={}
        for i in target:
            if i in h1:
                h1[i]+=1
            else:
                h1[i]=1
        
        for i in arr:
            if i in h2:
                h2[i]+=1
            else:
                h2[i]=1
        
        return h1==h2
        

s=Solution()
s.canBeEqual(target = [1,2,3,4], arr = [2,4,1,3])
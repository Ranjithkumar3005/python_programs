class Solution(object):
    def findPeaks(self, mountain):
        """
        :type mountain: List[int]
        :rtype: List[int]
        """
        dummy=[]
        for i in range(1,len(mountain)-1):
            if mountain[i]>mountain[i-1] and mountain[i]>mountain[i+1]:
                dummy.append(i)
        
        print(dummy)
s=Solution()
s.findPeaks(mountain = [1,4,3,8,5])
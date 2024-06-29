class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        c=0
        arr=sorted(heights)
        for i in range(0,len(heights)):
            if arr[i]!=heights[i]:
                c+=1
        print(c)
        
s=Solution()
s.heightChecker(heights = [1,2,3,4,5])
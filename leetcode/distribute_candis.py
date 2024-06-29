class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        h={}
        for i in candyType:
            if i not in h:
                h[i]=1
        
        if len(candyType)/2<len(h):
            return int(len(candyType)/2)
        else:
            return len(h)
        
        
s=Solution()
print(s.distributeCandies(candyType = [1,1,2,3]))
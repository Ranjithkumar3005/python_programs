class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
       
        c=1
        res=0
        colors+=colors[:k-1]
        for i in range(1,len(colors)):
            if colors[i]!=colors[i-1]:
                c+=1
            else:
                c=1
            if c>=k:
                res+=1
        
        return (res)
        
        
        
s=Solution()
print(s.numberOfAlternatingGroups(colors = [0,1,0,0,1,0,1], k = 6))
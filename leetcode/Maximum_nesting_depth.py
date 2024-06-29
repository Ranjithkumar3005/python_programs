class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        c=0
        for i in s:
            if i=="(":
                c+=1
                res=max(res,c)
            elif i==")":
                c-=1
        return res
        
s=Solution()
print(s.maxDepth(s = "(1+(2*3)+((8)/4))+1"))
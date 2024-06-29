class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        h={}
        for i in words:
            for j in i:
                if j in h:
                    h[j]+=1
                else:
                    h[j]=1
        
        for i in h:
            if h[i]%len(words)!=0:
                return False
        return True
        
s=Solution()
print(s.makeEqual( words = ["abc"]))
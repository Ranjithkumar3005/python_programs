class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        h={}
        for i in text:
            if i  in h:
                h[i]+=1
            else:
                h[i]=1
        count=1000000
        for i in "balon":
            if i not in h:
                return 0
            else:
               if i in ['l','o']:
                   h[i]/=2
               count=min(count,h[i]) 
        print(count)
        
        
s=Solution()
s.maxNumberOfBalloons(text = "loonbalxballpoon")
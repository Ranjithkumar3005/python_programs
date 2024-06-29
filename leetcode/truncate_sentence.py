class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        strs=""
        dum=s.split(" ")
        for i in range(0,k):
            if i!=k-1:
               strs+=dum[i]+" "
            else:
                strs+=dum[i]
        print(strs) 
            
        
        
s=Solution()
s.truncateSentence( s = "Hello", k = 1)
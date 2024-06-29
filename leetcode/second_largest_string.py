class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=[]
        st="ss"
        for i in s:
            if i.isdigit() and i not in n:
                n.append(i)
        if len(n)<2:
            return -1
        else:
            n=sorted(n)
            return n[len(n)-2]
        
        

s=Solution()
print(s.secondHighest( s = "abc1111"))
class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        check=False
        d=0
        for i in range(0,len(s)):
            if s[i]=="X":
                check=True
            if check:
                d+=1
            if d==3:
                check=False
                c+=1
                d=0
        if d>0:
            c+=1
        print(c)
        

s=Solution()
s.minimumMoves(s = "XXX")
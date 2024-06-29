class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        for i in range(1,1):
            print(i)
        dum=[]
        strs=""
        for i in range(ord(s[0]),ord(s[-2])+1):
            for j in range(int(s[1]),int(s[-1])+1):
              strs=chr(i)+str(j)
              dum.append(strs)
              strs=""
        print(dum)  
        
s=Solution()
s.cellsInRange(s = "K1:L2")
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        val=0
        for i in range(0,len(columnTitle)):
            val1=ord(columnTitle[i])-ord("A")+1
            print(val1)
            val*=26
            val+=val1
        
        print(val)
            
        
        

s=Solution()
s.titleToNumber(columnTitle = "ZY")
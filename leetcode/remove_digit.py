class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        dum=[]
        
        for i in range(0,len(number)):
            if number[i]==digit:
                val=number[:i]+number[i+1:]
                dum.append(int(val))
        dum=sorted(dum)
        print(dum[-1])

s=Solution()
s.removeDigit(number = "1231", digit = "1")
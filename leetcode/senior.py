class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        count=0
        for i in range(0,len(details)):
            if int(details[i][11:13])>=60:
                count+=1
        return count
        
s=Solution()
print(s.countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))
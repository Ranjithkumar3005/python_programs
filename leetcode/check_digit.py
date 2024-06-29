class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i in range(0,len(num)):
            if int(num[i])!=num.count(str(i)):
                return False
        return True
        
        
s=Solution()
print(s.digitCount(num = "1210"))
class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check=False
        for i in s:
            if i=="b":
                check=True
            if check and i=="a":
                return False
        return True
    
s=Solution()
print(s.checkString(s = "bbab"))
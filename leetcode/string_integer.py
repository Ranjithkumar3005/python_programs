class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        dummy=""
        s+="p"
        l="1 2 3 4 5 6 7 8 9 0 - +"
        for i in range(0, len(s)):
            if s[i] in l:
                dummy+=s[i]
                if s[i+1] not in l:
                    break
        if dummy.replace(" ","")=="":
            dummy="0"
        dummy1=int(dummy)       
        if dummy1<-2**31:
            dummy1=-2**31
        elif dummy1>2**31-1:
            dummy1=2**31-1
        return dummy1
                
s=Solution()
print(s.myAtoi("words a    987"))
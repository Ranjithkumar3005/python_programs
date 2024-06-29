class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        strs=""
        i=len(s)-1

        while i!=-1:
            if s[i]=="#":
                strs+=chr(96+int(s[i-2:i]))
                i=i-2
            elif int(s[i])<10:
                strs+=chr(96+int(s[i]))
            i-=1
        print(strs[::-1])
        

s=Solution()
s.freqAlphabets( s = "10#11#12")
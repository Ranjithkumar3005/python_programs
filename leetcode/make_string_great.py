class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        st=[]
        for i in range(0,len(s)):
            if st!=[] and (ord(s[i])+32==ord(st[len(st)-1]) or ord(s[i])-32==ord(st[len(st)-1])):
                print(s[i])
                st.pop()
            else:
                st.append(s[i])
        return "".join(st)
        
        
        
        
s=Solution()
print(s.makeGood(s = "lEetcode"))
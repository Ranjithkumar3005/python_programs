class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        str=s.split(" ")
        st=""
        print(str)
        for i in range(len(str)-1,-1,-1):
            if str[i]!="":
                st=st+str[i]+" "
        print(st.strip())

s=Solution()
s.reverseWords(s = "a good   example")
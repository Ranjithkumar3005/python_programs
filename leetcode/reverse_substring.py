class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        st=[]
        dum=""
        for i in s:
            if i==")":
                for j in range(len(st)-1,-1,-1):
                    print(st[j])
                    if st[j]=="(":
                        st.pop()
                        break
                    else:
                        dum+=st[j]
                        st.pop()
                for k in dum:
                    st.append(k)
                dum=""
            else:
                st.append(i)
        print("".join(st))
        

s=Solution()
s.reverseParentheses( s = "(abcd)")
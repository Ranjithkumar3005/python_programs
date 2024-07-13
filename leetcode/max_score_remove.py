class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        st=[]
        tot=0
        check=False
        if x>y:
            check=True
        for i in range(0,len(s)):
            dum="" 
            st.append(s[i])
            if len(st)>=2:
                dum=st[len(st)-2]+st[len(st)-1]
                print(dum)
                if check and dum=="ab":
                    tot+=x
                    st.pop()
                    st.pop()
                elif not check and dum=="ba":
                    tot+=y
                    st.pop()
                    st.pop()
        for i in range(len(st)-2,-1,-2):
            dum=st[i]+st[i+1]
            if not check and dum=="ab":
                    tot+=x
                    st.pop()
                    st.pop()
            elif check and dum=="ba":
                    tot+=y
                    st.pop()
                    st.pop()
        print(tot)
                          
s=Solution()
s.maximumGain(  s = "aabbaaxybbaabb", x = 5, y = 4)

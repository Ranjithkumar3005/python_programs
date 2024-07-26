class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        st=[]
        spli=path.split("/")
        
        for i in range(0,len(spli)):
            if spli[i]=="" or spli[i]==".":
                continue
            elif spli[i]=="..":
                if st:
                  st.pop()
            else:
                st.append(spli[i])
        print(st)
        str1="/"
        for i in range(0,len(st)):
            str1=str1+st[i]
            if i!=len(st)-1:
                str1+="/"
        print(str1)

s=Solution()
s.simplifyPath(  path ="/../")
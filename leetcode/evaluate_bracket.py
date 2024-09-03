class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        
        str2=""
        inx=0
        check=True
        h={}
        for i in knowledge:
            h[i[0]]=i[1]
        for i in range(0,len(s)):
            if s[i]=="(":
                inx=i+1
                check=False
            if check:
                str2+=s[i]
            if s[i]==")":
                str1=s[inx:i]
                if str1 in h:
                    str2+=h[str1]
                else:
                    str2+="?"
                check=True
                    
        print(str2)

s=Solution()
s.evaluate( s = "hi(name)", knowledge = [["a","b"]])
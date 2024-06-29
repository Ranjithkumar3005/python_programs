class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        h={}
        strs=""
        check=True
        dummy=False
        for i in range(0,len(emails)):
            for j in range(0,len(emails[i])):
                if emails[i][j]=="@":
                    check=False
                    dummy=False
                    strs+=emails[i][j]
                elif dummy:
                    continue
                elif emails[i][j]=="." and check:
                    continue
                elif emails[i][j]=="+" and check:
                    dummy=True
                else:
                    strs+=emails[i][j]
            print(strs)
            if strs not in h:
                h[strs]=1
            strs=""
            check=True
            dummy=False
        return len(h)
s=Solution()
print(s.numUniqueEmails(emails =["a@e+c.com", "a@e+c+f.com"]))
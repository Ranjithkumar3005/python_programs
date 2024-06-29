class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        dum=title.split(" ")
        strs=[]
        for i in dum:
            if len(i)>2:
                strs.append(i.title())
            else:
                strs.append(i.lower())
        return " ".join(strs)
        
s=Solution()
print(s.capitalizeTitle(title = "First leTTeR of EACH Word"))
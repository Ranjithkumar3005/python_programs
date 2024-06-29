class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        dum=s.split(" ")
        dumm1=[0]*len(dum)
        for i in dum:
            print(dumm1)
            dumm1[int(i[len(i)-1])-1]=i[0:len(i)-1]
        return " ".join(dumm1)

        
s=Solution()
print(s.sortSentence(s = "is2 sentence4 This1 a3"))
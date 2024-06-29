class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        h={"a":1,"e":1,"i":1,"o":1,"u":1,"A":1,"E":1,"I":1,"O":1,"U":1}
        i=0
        j=len(s)-1
        c=0
        while c!=len(s) and i!=j:
            print(c," ",i,' ',j)
            if s[i] in h:
                if s[j] in h:
                    dum=s[j]
                    s[j]=s[i]
                    s[i]=dum
                    i+=1
                    j-=1
                    c+=2
                else:
                    j-=1
                    c+=1
            else:
                i+=1
                c+=1
        print("".join(s))
s=Solution()
s.reverseVowels(s = "aA")
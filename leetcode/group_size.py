class Solution:
    def hasGroupsSizeX(self, deck):
        h={}
        for i in deck:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        val=list(h.values())
        print(val)
        gcd1=val[0]
        for i in range(1,len(val)):
            gcd1=gcd(gcd1,val[i])
        if val==1:
            return False
        return True

s=Solution()
s.hasGroupsSizeX(deck = [1,2,3,4,4,3,2,1])
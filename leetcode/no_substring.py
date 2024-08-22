class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        h={}
        c=0
        s+="0"
        for i in s:
            if i=="1":
              c+=1
            elif c!=0:
                if c in h:
                    h[c]+=1
                else:
                    h[c]=1
                c=0
             
        sum=0
        for i in h:
            c1=0
            for i in range(1,i+1):
                c1+=i
            sum+=(c1*h[i])
        print(sum)
        

s=Solution()
s.numSub(s = "0110111")
class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        h={"a":0,"e":0,"i":0,"o":0,"u":0}
        h1={"a":[],"e":[],"i":[],"o":[],"u":[]}
        max1=0
        c=0
        for i in range(0,len(s)):
            if s[i] in h1:
                h1[s[i]].append(i)
        print(h1)
        tot=[]
        min1=999999999
        max1=0
        for i in h1:
            if h1[i]==[]:
                continue
            if len(h1[i])%2==0:
                min1=min(min1,min(h1[i]))
                max1=max(max1,max(h1[i]))
                tot.append(max1-min1)
            elif len(h1[i])>2:
                min1=h1[i][1]
                max1=max(max1,max(h1[i]))
                tot.append(max1-min1)
        print(tot)       
            
            
                 

s=Solution()
s.findTheLongestSubstring(s = "eleetminicoworoep")
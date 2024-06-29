class Solution(object):
    def getLengthOfOptimalCompression(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dummy=[]
        strs=""
        h={}
        for i in range(0,len(s)):
            dummy.append(s[i])
        for i in range(97,123):
            if chr(i) in dummy:
                h[chr(i)]=s.count(chr(i))
                if s.count(chr(i))!=1:
                    strs+=chr(i)+str(s.count(chr(i)))
                else:
                    strs+=chr(i)
        
        print(strs)
        print(h)
        count=0
        count1=0
        dummy1=0
        dummy3=[]
        
        for key in h:
            if h[key]==k:
                count+=k
                dummy3.append(count)
            elif h[key]<k:
                dummy1+=k
                if dummy1==k:
                   dummy3.append(dummy1)
                   k=0
        
        if dummy3!=[]:return min(dummy3)
        return len(strs)
        
s=Solution()
print(s.getLengthOfOptimalCompression( s = "a", k = 1))
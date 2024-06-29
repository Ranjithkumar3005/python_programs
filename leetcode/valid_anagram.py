class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        print(s," ",t)
        dummy=[]
        count=0
        dummy1=True
        for i in s:
            dummy.append(i)
        for i in t:
            if i in dummy:
                count+=1
                dummy.remove(i)
        
        if count!=len(s) or count!=len(t):
            dummy1=False
        return dummy1
        
s=Solution()
print(s.isAnagram(s = "t", t = "at"))
class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        h={}
        dummy=[]
        for i in s:
            dummy.append(i)
        for i in s:
            if ord(i)>64 and ord(i)<91 and i not in h and chr(ord(i)+32) in dummy:
                h[i]=ord(i)
                
        if h!={}:
            ma=max(list(h.values()))
            for i in h:
                if h[i]==ma:
                    return i
        return ""
        
s=Solution()
print(s.greatestLetter(s = "arRAzFif"))
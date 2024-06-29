class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        
        h={}
        str=""
        for i in range(0,len(order)):
            h[i]=order[i]
        
        for i in h:
            if h[i] in s:
                str+=h[i]*s.count(h[i])
                
        for i in s:
            if i not in h.values():
                str+=i
        print(str)
        

s=Solution()
s.customSortString(order = "bcafg", s = "abcd")
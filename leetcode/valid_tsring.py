class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        dummy=0
        i=0
        while i<len(haystack):
            if needle[dummy]==haystack[i]:
                #print(i)
                dummy+=1
            else:
                i=i-(dummy-1)
                dummy=0
                continue
            if dummy==len(needle):
                return i-(len(needle)-1)  
            i+=1          
        return -1
        
s=Solution()
print(s.strStr(haystack = "mississippi", needle = "issi"))
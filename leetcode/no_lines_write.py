class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        count=0
        count1=0
        dummy=[]
        for i in range(0,len(s)):
            count+=widths[ord(s[i])-97]
            if count>100:
                count-=widths[ord(s[i])-97]
                dummy.append(count)
                count=widths[ord(s[i])-97]
        dummy.append(count)
        return [len(dummy),dummy[len(dummy)-1]]
        
s=Solution()
print(s.numberOfLines( widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"))
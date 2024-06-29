class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        dummy=""
        dummy1=True
        count=1
        for i in range(len(num)-1,-1,-1):
            if num[i]=='0' and dummy1:
                count+=1
                continue
            else:
                dummy1=False
                dummy+=num[len(num)-i-count]
        print(dummy)
        
s=Solution()
s.removeTrailingZeros(num = "512301009")
class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        h={}
        count=0
        max=-1
        for i in range(0,len(s)):
            if s[i] not in h:
                h[s[i]]=i
            else:
                count=i-h[s[i]]-1
                if max<count:
                    max=count
                count=0
        return max
s=Solution()
print(s.maxLengthBetweenEqualCharacters("mgntdygtxrvxjnwksqhxuxtrv"))
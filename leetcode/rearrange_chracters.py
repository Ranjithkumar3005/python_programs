from collections import Counter


class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: intA
        """
        counter_s = Counter(s)        
        return min(counter_s[c] // count for c,count in Counter(target).items())
s=Solution()
print(s.rearrangeCharacters(s = "ilovecodingonleetcode", target = "code"))
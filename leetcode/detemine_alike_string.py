class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count1=0
        count2=0
        for i in range(0,int(len(s)/2)):
            if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                count1+=1
        for i in range(len(s)-1,int(len(s)/2)-1,-1):
            if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                count2+=1
        if count1==count2:
            return True
        return False

s=Solution()
print(s.halvesAreAlike(s = "book"))
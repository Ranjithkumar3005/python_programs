class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret=0
        count=0
        for i in s:
            if i=="L":
                ret+=1
            else:
                ret-=1
            if ret==0:
                count+=1
        return count
        
        

s=Solution()
print(s.balancedStringSplit( s = "RLRRRLLRLL"))
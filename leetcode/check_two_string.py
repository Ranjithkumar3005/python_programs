class Solution(object):
    def canBeEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        dummy1=""
        dummy=s1[2]+s1[1]+s1[0]+s1[3]
        if s1[0]==s2[0]:
            dummy1=s1[0]+s1[3]+s1[2]+s1[1]
        else:
            dummy1=dummy[0]+dummy[3]+dummy[2]+dummy[1]
        if dummy==s2 or dummy1==s2:
            return True
        else:
            return False        
        
s=Solution()
print(s.canBeEqual(s1 ="bnxw",s2 ="bwxn"))
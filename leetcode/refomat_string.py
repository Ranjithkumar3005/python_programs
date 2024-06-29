class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        dummy1=[]
        dummy2=[]
        for i in s:
            if i.isalpha():
                dummy1.append(i)
            else:
                dummy2.append(i)
        strs=""
        if len(dummy1)==len(dummy2):
            for i in range(0,len(dummy1)):
               strs+=dummy2[i]+dummy1[i]
        elif len(dummy1)-1==len(dummy2):
            for i in range(0,len(dummy2)):
               strs+=dummy1[i]+dummy2[i]
            strs+=dummy1[len(dummy1)-1]
        elif len(dummy1)==len(dummy2)-1:
            for i in range(0,len(dummy1)):
               strs+=dummy2[i]+dummy1[i]
            strs+=dummy2[len(dummy2)-1]
        return strs
        
s=Solution()
print(s.reformat(s = "covid201990"))
class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        str1=""
        for i in s:
            if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90):
                str1+=i
        
        str1=str1[::-1]
        c=0
        str2=""
        for i in s:
            if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90):   
                str2+=str1[c]
                c+=1
            else:
                str2+=i
        print(str2)        

s=Solution()
s.reverseOnlyLetters(s = "a-bC-dEf-ghIj")
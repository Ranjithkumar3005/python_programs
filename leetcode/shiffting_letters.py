class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        sum=[]
        shifts.reverse()
        su=0
        for i in range(0,len(shifts)):
            su+=shifts[i]
            sum.append(su)
        
        sum.reverse()
        str1=""
        for i in range(0,len(s)):
            val=((ord(s[i])-97+(sum[i]))%26)+97
            str1+=chr(val)
        print(str1)  
        

s=Solution()
s.shiftingLetters(s = "ruu", shifts = [26,9,17])
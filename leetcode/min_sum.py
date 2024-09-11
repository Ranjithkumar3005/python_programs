class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        dum=[]
        num=str(num)
        for i in num:
            dum.append(int(i))
        dum=sorted(dum)
        arr=[]
        num1=int(str(dum[0])+str(dum[3]))
        num2=int(str(dum[1])+str(dum[2]))
        return num1+num2
        

s=Solution()
print(s.minimumSum(num = 2932))
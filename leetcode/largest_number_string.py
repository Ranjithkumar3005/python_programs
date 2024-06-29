class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        dummy="p"
        dummy1=[]
        for i in range(0,len(num)):
            if dummy[0]!=num[i]:
                dummy=""
                dummy+=num[i]
            else:
                dummy+=num[i]
            if len(dummy)==3:
                 dummy1.append(str(dummy))
        dummy1.sort()
        if len(dummy1)!=0:
            print(str(dummy1[len(dummy1)-1]))
        return ""
s=Solution()
s.largestGoodInteger("23333017779")
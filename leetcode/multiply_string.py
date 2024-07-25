class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        num1,num2=num1[::-1],num2[::-1]
        result=[0]*(len(num1)+len(num2))
        print(result)
        for i in range(len(num1)):
            for j in range(len(num2)):
                product=int(num1[i])*int(num2[j])
                result[i+j]+=product
                result[i+j+1]+=result[i+j]//10
                result[i+j]%=10
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return "".join(map(str, result[::-1]))
        

s=Solution()
print(s.multiply(num1 = "123", num2 = "456"))
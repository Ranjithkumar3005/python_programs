class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        strs=""
        dummy=[]
        for i in digits:
            strs+=str(i)
        intr=str(int(strs)+1)
        for i in intr:
            dummy.append(int(i))
        print(dummy)
s=Solution()
s.plusOne(digits = [9])
class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        count=0
        for i in logs:
            if i=="./":
                continue
            elif i=="../":
                if count!=0:count-=1
            else:
                count+=1
            
        return count
s=Solution()
print(s.minOperations(["./","../","./"]))
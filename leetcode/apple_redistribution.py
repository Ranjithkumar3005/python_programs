class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        sum1=sum(apple)
        capacity=sorted(capacity,reverse=True)
        sum2=0
        c=0
        for i in range(0,len(capacity)):
            sum2+=capacity[i]
            c+=1
            if sum2>=sum1:
                return c
        

s=Solution()
print(s.minimumBoxes(apple = [1,3,2], capacity = [4,3,1,5,2]))
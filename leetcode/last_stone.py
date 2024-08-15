class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones=sorted(stones)
        while len(stones)>1:
            val1=stones.pop()
            val2=stones.pop()
            if val1!=val2:
                stones.append(val1-val2)
                stones=sorted(stones)
            
        print(stones[0])

s=Solution()
s.lastStoneWeight(stones = [2,7,4,1,8,1])